# gBizINFO 変化シグナル パイプライン

経済産業省 gBizINFO から、企業ごとの**補助金採択・官公庁調達・届出認定・表彰**を日次で取得し、
「前回の実行以降に新しく現れたもの」だけを抽出して蓄積します。

売り物は企業リストではなく**変化**です。補助金を採択された直後の企業は、その予算の使い先を
探している状態にあり、士業・コンサル・設備業者・SaaS 事業者にとって最も接触価値が高い瞬間にいます。

## 法的な位置づけ

一次ソースは gBizINFO のみで、スクレイピングは一切していません。

gBizINFO は**政府標準利用規約 2.0** に準拠しており、出典を明記すれば**商用利用・改変・二次配布が
すべて認められています**。生成物には自動的に出典表記が入ります（`main.py` の `attribution`）。

> 出典: gBizINFO（経済産業省） https://info.gbiz.go.jp/

API 利用は**申請時に申告した目的の範囲に限定される**ため、商用利用を明記して申請してください。

## セットアップ

1. https://info.gbiz.go.jp/ から API 利用を申請する（無料・審査あり・**利用目的に商用利用を明記**）
2. 発行されたトークンを環境変数に設定する

```bash
export GBIZINFO_API_TOKEN="発行されたトークン"
pip install -r ../requirements.txt
```

GitHub Actions で回す場合は、リポジトリの **Settings → Secrets and variables → Actions** に
`GBIZINFO_API_TOKEN` を登録してください。未設定でもワークフローは警告を出して正常終了します
（失敗通知が毎日飛ぶのを避けるため）。

## 最初にやること: 前提の検証

**この事業の成否は「gBizINFO が日次で意味のある量の変化を出しているか」の一点にかかっています。**
トークンが届いたら、他のどのコードより先にこれを実行してください。

```bash
python -m gbiz.probe --months 12
```

過去 12 か月を月ごとにさかのぼり、種別ごとの件数と、API がレコードに付けている
`import_frequency`（元データの取込頻度）を集計します。出力例：

```
  subsidy        median/month=4210      max=9880     months_with_data=12
                 import_frequency={'毎月': 100}
  procurement    median/month=1530      max=2210     months_with_data=12

  viable for a daily signal : ['subsidy', 'procurement']
  too thin                  : ['commendation']
```

判定基準は月 30 件（≒1 日 1 件）です。これを下回る種別は、日次通知として送るものが
ほとんどの日に存在しないため、商品になりません。

**`import_frequency` が「毎月」なら、日次で叩いても情報の鮮度は上がりません。**
その場合は日次配信をやめ、更新検知の即時通知に設計を変える必要があります。

## 日次実行

```bash
python -m gbiz.main --lookback-days 7
python -m gbiz.main --dry-run          # 取得だけして書き込まない
```

さかのぼり幅を 7 日にしているのは、gBizINFO が過去日付の情報を後から追加することがあるためです。
重複は `event_id` で排除されるので、幅を取っても件数は増えません。

## 出力

```
gbiz_data/
  events/YYYY-MM.jsonl   観測した全イベント（追記のみ）。イベント発生月で分割
  state/seen.json        event_id → {first_seen, last_seen, content_hash}
  daily/YYYY-MM-DD.json  その日のシグナル（新規 + 改訂）
  latest.json            最新の実行結果
```

`daily/` の各ファイルがそのまま商品の中身です。`new_events` が新規に現れたイベント、
`top_new_events_by_amount` が金額上位 50 件です。

## 構成

| ファイル | 役割 |
| --- | --- |
| `client.py` | API クライアント。ページング、リトライ、レート制御 |
| `normalize.py` | 入れ子の法人レコードを 1 イベント 1 行に平坦化 |
| `store.py` | 追記型ストアと初回観測日の管理。**新規判定の中核** |
| `probe.py` | 前提検証。事業の可否を判定する |
| `main.py` | 日次実行のエントリポイント |
| `test_gbiz.py` | オフラインテスト。**トークン無しで全て実行可能** |

```bash
python -m unittest gbiz.test_gbiz -v
```

## 設計上の判断

**なぜ `event_id` をハッシュで作るのか。** gBizINFO のイベントには主キーがありません。
そこで「法人番号・種別・事業名・日付・金額・府省」の組を同一性の定義としています。
これにより、同じ期間を何度取得しても重複しません。

**なぜ「改訂」を新規と分けるのか。** 金額の訂正や事業名の変更は、新規採択とは価値が違います。
`content_hash` の変化で検出し、`first_seen` は初回観測日のまま保持します。

**なぜ蓄積するのか。** API の `updateInfo` は `from`/`to` で過去を引けるため、履歴そのものは
誰でも取得できます。蓄積の価値は履歴の独占ではなく、(1) 正規化済みで即座に配信できる状態を
保つこと、(2) 「いつ我々が観測したか」という API には存在しない情報を持つこと、の 2 点です。

## 未検証の前提

- **元データの更新頻度**（`probe.py` で判定する。事業の成否を分ける最大の変数）
- **レート制限の実際の閾値**。公式仕様に記載がないため `min_interval=1.0` 秒で保守的に運用
- **`updateInfo` の `from`/`to` にさかのぼれる上限**。過去 12 か月を引けるかは probe で判明する

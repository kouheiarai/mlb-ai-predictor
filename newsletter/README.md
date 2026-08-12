# Japan Money Weekly

英語圏向けの日本経済ニュースレターを、リサーチから本文執筆まで自動で生成する仕組み。

Claude（`claude-opus-5`）に Web 検索させて一次情報を集めさせ、`prompts/` の編集方針に従って
本文 HTML まで書かせる。生成物は `state/issues/` に残り、そのまま beehiiv に貼れる。

## 何を書くニュースレターか

**日本の家計金融資産がどこへ動いているか**を軸に、3 種類の号を出し分ける。

| 号種 | 頻度 | 中身 |
|---|---|---|
| `weekly` | 毎週 | 家計金融資産・NISA・資金フロー・関連政策 |
| `boj` | 年 8 回 | 日銀の金融政策決定会合。声明文の**前回との差分**を取って解説する |
| `shunto` | 1〜4 月 | 春闘の賃上げ交渉を追う季節シリーズ |

`boj` と `shunto` は単体では配信頻度が足りないが、`weekly` に束ねることで週次が埋まり、
年 8 回と年 1 回の「目玉号」として機能する。号種は実行日から自動判定される。

## 2つの動かし方

| | 手動モード | API モード |
|---|---|---|
| 費用 | **無料** | 1 号 $0.30〜0.60（週1で月 $2〜3） |
| 手間 | 毎週 5〜10 分の貼り付け作業 | ゼロ（GitHub Actions が自動実行） |
| 必要なもの | ブラウザの Claude | Anthropic の API キー |

**成果物はどちらも同じ**。重複防止の履歴も共通なので、手動で始めて後から API に切り替えても
それまでの号はすべて引き継がれる。まず手動モードで品質を確かめ、続けられそうなら API に
移行するのが安全。

## 手動モード（無料）

```bash
cd newsletter
pip install PyYAML          # anthropic SDK は不要
python generate.py --print-prompt > prompt.txt
```

1. `prompt.txt` の中身をまるごと [claude.ai](https://claude.ai) に貼る
2. **リサーチ（Web 検索）を有効にして**送る
3. 返ってきた応答を**まるごと** `response.txt` に保存する（`===TITLE===` から最後まで）
4. 取り込む:

```bash
python ingest.py response.txt
```

`--print-prompt` は号種と、そのまま実行できる `ingest.py` のコマンドを画面に表示する。
日銀号や春闘号を試すときは `--type boj` などを両方のコマンドに付ける。

## API モード（自動）

```bash
cd newsletter
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
```

まず 1 号ぶん、保存せずに生成して中身を確認する:

```bash
python generate.py --dry-run
```

問題なければ保存する:

```bash
python generate.py
```

`state/issues/YYYY-MM-DD-<slug>.md`（レビュー用。出典と本文を含む）と `.html`（beehiiv 貼り付け用）
が生成される。

### 号種を指定して試す

```bash
python generate.py --type boj --dry-run
python generate.py --type shunto --dry-run
```

## 運用フロー（現在：無料プラン）

beehiiv の投稿 API は **Max / Enterprise プラン限定**なので、無料枠のあいだは自動投稿しない。

1. GitHub Actions が毎週水曜 08:00 JST に実行され、下書きを生成してリポジトリにコミットする
2. `state/issues/` の最新 `.md` を読んでレビューする
3. 問題なければ `.html` の中身を beehiiv のエディタに貼り付けて配信する

### レビューは日本語サマリーから読む

配信するのは英語だが、`.md` の先頭には**日本語のレビュー用サマリー**が付く。ここだけ読めば
公開可否を判断できるように設計してある。

- **この号の主張** — 結局なにを言っている号なのか
- **使った数字と出典の対応** — 本文の数値がすべて出典に紐づいているか
- **確信度が低い箇所** — 検証しきれなかった点。まずここを見る
- **コンプライアンス自己点検** — 銘柄推奨・価格予想が混入していないか

このサマリーは beehiiv には送られない（`.html` には含まれない）。英語本文を一行ずつ読み直さ
なくても、事実関係とコンプライアンスを数分で確認できる。

## 読者 100 人を超えたら

beehiiv を Max プランに上げたうえで:

1. beehiiv の管理画面で API キーと Publication ID を発行する
2. GitHub の Secrets に `BEEHIIV_API_KEY` と `BEEHIIV_PUBLICATION_ID` を登録する
3. `config.yaml` の `publish.mode` を `local` → `draft` に変える

これで**下書きまで全自動**になり、beehiiv 上で公開ボタンを押すだけになる。
運用が安定してから `confirmed` に変えれば完全自動配信になる。

> `status` は常に明示的に送っている。2026-08-06 以降、beehiiv は `status` 省略時に下書き扱いに
> なる仕様に変わったため、省略に頼らない。

## 最初にやるべき設定：日銀の会合日程

`config.yaml` の `issue_types.boj.meeting_dates` は**空のまま出荷している**。ここが空だと
日銀号は一度も発火せず、通常号だけが出続ける。

日銀が公表している金融政策決定会合の日程から、各会合の**最終日**を年 8 回ぶん転記すること。

- https://www.boj.or.jp/mopo/mpmsche_minu/index.htm

```yaml
boj:
  meeting_dates:
    - "2026-09-19"
    - "2026-10-31"
```

年に一度の作業なので自動化していない。

## コスト

1 号あたりおよそ **$0.30〜0.60**（入力 $5 / 出力 $25 per 1M トークン、Web 検索 1000 回で $10）。
週 1 回なら**月 $2〜3 程度**。実行のたびに実測値と概算コストが出力される。

`prompts/house_style.md` は毎号同一なのでプロンプトキャッシュに載せてあり、2 号目以降は
その部分の入力コストが約 1/10 になる。

GitHub Actions は 1 回あたり数分〜十数分で、無料枠（月 2,000 分）にはまったく届かない。

## 構成

```
newsletter/
├── config.yaml            運用設定はすべてここ。コードは触らない
├── generate.py            リサーチ → 執筆 → 保存 → 配信（--print-prompt で手動モード）
├── ingest.py              claude.ai の応答を取り込む（手動モード用）
├── beehiiv.py             Create Post API のクライアント
├── prompts/
│   ├── house_style.md     編集方針・文体・正確性ルール・出力フォーマット（毎号共通）
│   ├── weekly.md          通常号
│   ├── boj.md             日銀号（声明文の差分を取らせる）
│   └── shunto.md          春闘号
└── state/
    ├── topics.json        配信済みタイトルとトピックの履歴（重複防止に使う）
    └── issues/            生成された号
```

### `state/topics.json` を消さないこと

過去号のタイトルと扱ったトピックを毎回プロンプトに差し戻して、同じ話を書かせないようにしている。
これを消すと数ヶ月後から同じネタの焼き直しが始まる。`config.yaml` の `dedup.lookback` で
何号ぶん参照するかを変えられる。

## 品質を変えたいとき

コードではなく `prompts/` を編集する。

- 文体・正確性ルール・出力フォーマット → `house_style.md`
- 通常号の取材範囲・ネタの選び方 → `weekly.md`
- リサーチを厚くしたい → `config.yaml` の `model.max_web_searches` と `model.effort`

`house_style.md` には**投資助言にならないための制約**（個別銘柄の推奨をしない、価格予想をしない、
将来見通しは必ず発言者に帰属させる）を明記してある。ここは外さないこと。

## 独立リポジトリへ移すとき

この `newsletter/` ディレクトリは MLB 予測プロジェクトから完全に独立していて、依存関係もない。
そのままコピーすれば単独リポジトリとして動く。`.github/workflows/newsletter.yml` の
`working-directory` と `cache-dependency-path` からパスを外すだけでよい。

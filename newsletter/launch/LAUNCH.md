# 1号目を出すための手順と文面

`state/issues/` の1号目を実際に配信するまでに必要なものを、そのまま使える形でまとめてある。
英語の文面はコピーして使う前提。日本語の部分は説明。

---

## 1. beehiiv の設定

無料の Launch プランで始める。読者 2,500 人まで課金されない。

| 項目 | 入れる値 |
|---|---|
| Publication name | `Japan Money Weekly` |
| Subdomain | `japanmoneyweekly`（独自ドメインは後からでよい） |
| Description | 下の「Publication description」をそのまま |
| Language | English |
| Sending schedule | 手動送信（自動化するのは Max に上げてから） |

### 貼り付け時の注意

1. `state/issues/` の `.html` を開いて中身を全部コピーする
2. beehiiv のエディタで**ソース/HTML 入力モード**に切り替えてから貼る
   （通常のエディタに貼るとタグがそのまま文字として出る）
3. `&#165;` は正しい。直さない。プレビューで `¥` として表示される
4. **プレビューをスマホ表示で必ず確認する**。本文に表が1つ入っているので、
   崩れていたら表をやめて箇条書きに直す（メールでの表組みは環境差が出やすい）

---

## 2. Publication description

登録ページとディレクトリに出る紹介文。

```
Where Japan's money is actually moving — reported from Japanese sources, in plain English.

Japanese households sit on nearly ¥2.4 quadrillion, and it has started to move for the first
time in a generation. Every Wednesday, one story about where it is going: the flow of funds data,
the NISA numbers, the Bank of Japan, and the wage round that decides all of it.

For investors and finance people outside Japan who keep reading about Japan and never quite get
the view from inside it.
```

---

## 3. ランディングページの文面

### Headline

```
Where Japan's money is actually moving.
```

### Subheadline

```
Japanese households hold nearly ¥2.4 quadrillion — about three and a half times everything Japan
produces in a year. After thirty years of sitting still, it has started to move. This is a weekly
read on where it goes, built from Japanese primary sources.
```

### What you get

```
• One story a week, reported properly — not a link roundup.
• Bank of Japan specials, eight times a year: what changed in the statement, word by word,
  against the previous one.
• The spring wage round, covered from January through April, when it actually decides what the
  Bank of Japan does next.
• Numbers you can check. Every figure is dated and sourced.
```

### Why this exists

```
English-language business media covers Japan in two modes: when it touches American interests, or
as a curiosity. Currency intervention and bullet trains. Neither one tells you what is happening
inside the world's fourth-largest economy, and neither one is written by someone reading the
Japanese releases.

This is the other thing.
```

### CTA

```
Free, every Wednesday. Unsubscribe whenever.
```

---

## 4. ウェルカムメール

beehiiv の Automations → Welcome email に設定する。登録直後に自動送信される。

**Subject**

```
You're in — here's what to expect
```

**Body**

```
Thanks for subscribing.

Japan Money Weekly lands on Wednesdays. One story, properly reported, about where Japanese money
is going — usually built from a Japanese-language release that has not been written up in English.

A few things worth knowing up front:

Every number is dated and sourced. If something could not be verified, the issue says so rather
than rounding it into a confident sentence.

This is reporting, not advice. You will never find a stock tip, a price target, or a "you should
buy" in here. What you get is what institutions and households actually did, and how the
mechanism works.

Eight times a year there is a Bank of Japan special: the policy statement compared word by word
against the previous one. That comparison is where the Bank actually signals its intentions, and
almost nobody outside Japan reads it.

One ask, and it genuinely shapes what gets written: hit reply and tell me what you are trying to
figure out about Japan. Currency? The wage round? Whether the household shift into equities is
real? I read all of them.

— [your name]
```

> 返信を求めているのは礼儀ではなく、**何を書くべきかを読者から直接聞くのが最短だから**。
> 初期の返信は、そのまま `prompts/weekly.md` の取材範囲に反映する価値がある。

---

## 5. 最初の読者をどこから連れてくるか

**ここが本当のボトルネック。** 仕組みも配信基盤も、読者ゼロの問題は解決しない。

### ⚠️ 先に読むこと

金融系の subreddit はほぼ例外なく**自己宣伝を制限している**。新規アカウントでリンクを貼ると
削除・BAN されて、一度きりの初回チャンスを無駄にする。

必ず次の順で進める。

1. 各 subreddit の Rules を読む。**要約を読むのではなく、全部展開して原文を読むこと。**
2. 迷ったら modmail で先に許可を取る（数日かかることもある）
3. **リンクも、ニュースレターへの言及も、本文に一切入れない**（理由は下）

### r/JapanFinance の規約を読んで分かったこと（2026-08 時点）

規約は7条。運用に直接効くのが2つある。

**規約5「勧誘や宣伝は一切行いません」**

> ビジネスを推奨したりレビューしたりするのは問題ありませんが、広告のようなコンテンツは
> 削除されます。また、**ダイレクトメッセージやその他の個人的なコミュニケーション
> （電子メール、オンラインフォームなど）の勧誘もお控えください。**

後半が重要。ニュースレターは定義上「メールアドレスの勧誘」である。したがって

- **本文の末尾に1行だけ置く、も禁止に当たる。**末尾でも勧誘は勧誘。
- 投稿にも、コメントにも、**ニュースレターの存在を書かない**。

代わりに、**プロフィール欄のリンクに働かせる**。投稿が良ければユーザー名は押される。
プロフィールは sub の外なので規約5の範囲外。これが唯一の安全な導線。

**規約7「Don't cite LLMs」**

- 「AI に聞いたら」「Claude によると」は書かない。出典は必ず一次資料（日銀、統計局など）。
- 規約は "cite" を禁じているが、実務上は**文章が LLM っぽいだけで疑われて沈む**。
  整いすぎた箇条書き、体言止めの多用、「Moreover」「Furthermore」は避ける。
  一人称で、少し粗く書く。

**規約3・4「専門家のアドバイスを求めない/提供しない」** は `prompts/house_style.md` の
コンプライアンス方針と同じ。個別の行動を処方せず、一般的な情報にとどめる。

**規約6**は米国納税者のみフレア設定が必要。該当しなければ無視。

### r/JapanFinance 向けの投稿文

**Title**

```
Household deposits are shrinking as a share of assets — but deposits as a category are still growing
```

**Body**

```
I was going through the BOJ's Q1 2026 flow of funds release and the breakdown surprised me a lot
more than the headline did.

The number that got picked up was that cash and deposits fell to 47.2% of household financial
assets, from 47.6%. That share sat above 50% for decades, so it reads like the shift into risk
assets everyone has been waiting for.

Then I looked at the flows. Smoothed over four quarters, households added ¥5.8tn:

- Cash and deposits: +¥1.7tn
- Equities and investment trusts: +¥1.5tn (investment trusts alone +¥3.0tn)
- Debt securities: +¥1.3tn
- Insurance and pensions: +¥1.3tn

Deposits as a category are still growing. What's shrinking is specifically the liquidity deposit —
the ordinary account your salary lands in. The money is largely moving to time deposits, JGBs and
insurance. That's a rate story, not a risk-appetite story. Long-term lending rates crossed 2% in
June for the first time in 25 years.

The other bit worth noting: equities and investment trusts together took in ¥1.5tn while
investment trusts alone took in ¥3.0tn. So households are buying funds and net selling individual
shares.

And seasonally adjusted, households went to a net financial deficit (−¥1.3tn from +¥4.9tn).
Dai-ichi Life is cautious about reading much into that since the adjusted series swings hard, but
it's an unusual print for a sector that's been in surplus for decades.

Curious whether anyone here has actually moved cash around since rates started moving.

Sources: BOJ flow of funds Q1 2026 (released 25 June), with commentary from Dai-ichi Life Research
Institute and NLI Research Institute.
```

**元の文面から変えた点**

| 変更 | 理由 |
|---|---|
| ニュースレターへの言及を全削除 | 規約5（メール勧誘の禁止） |
| 「came out」→「I was going through」 | 6月25日公表なので「出たばかり」は嘘になる |
| 末尾に読者への問いかけを追加 | 規約2の「協力的・建設的」に沿い、コメントが付きやすい |
| 出典に公表日を明記 | 数字の鮮度を読者が自分で判断できる |

投稿がついたら、コメント欄で質問に答える。**ここでの受け答えが、リンクより効く。**

### そのほかの流入源

| 場所 | 注意点 |
|---|---|
| r/investing, r/JapanLife | 同じくルール確認が必須。JapanFinance より宣伝に厳しいことがある |
| X（日本マクロ・為替クラスタ） | 表の画像1枚＋要点3行が最も伸びる。リンクは返信に置く |
| Hacker News | Show HN ではなく、記事そのものを submit する。タイトルは記事の見出しのまま |
| LinkedIn | 金融関係の知人がいるなら初期の 10〜20 人はここが確実 |

---

## 6. 何を見るか

最初の数号で追うのは購読者数ではなく、**続ける価値があるかどうかの判定材料**。

| 指標 | 見方 |
|---|---|
| 開封率 | 初期の小さいリストなら 40〜50% は出る。30% を切るなら件名かテーマがずれている |
| クリック率 | 出典リンクが踏まれているかは、内容を信用されている証拠になる |
| **返信数** | **最重要。** 1通でも返信が来たら、それは購読者100人より価値がある情報 |
| 登録の流入元 | どの投稿から来たかを beehiiv で確認し、効いた場所に集中する |

読者が増えないこと自体は問題ではない。**誰も返信しないことが問題**。その場合はテーマではなく
切り口を疑う。

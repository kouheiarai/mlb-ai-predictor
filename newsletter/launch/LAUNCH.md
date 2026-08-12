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

1. 各 subreddit の Rules と「self-promotion」に関する記載を読む
2. 迷ったら modmail で先に許可を取る（数日かかることもある）
3. **リンクではなく中身を投稿する。** 記事の要点を本文にそのまま書き、
   ニュースレターへの言及は末尾の1行にとどめる

宣伝として投稿すると失敗する。**発見を共有する投稿の末尾に出典として置く**と通る。

### r/JapanFinance 向け

**Title**

```
Japanese households pulled a record amount out of ordinary deposits last quarter — but most of it
didn't go into stocks
```

**Body**

```
The BOJ's Q1 2026 flow of funds came out and the headline everyone picked up was that cash and
deposits fell to 47.2% of household financial assets, from 47.6%. That share sat above 50% for
decades.

What I found more interesting is the breakdown. Smoothed over four quarters, households added
¥5.8tn:

- Cash and deposits: +¥1.7tn
- Equities and investment trusts: +¥1.5tn (investment trusts alone +¥3.0tn)
- Debt securities: +¥1.3tn
- Insurance and pensions: +¥1.3tn

Deposits as a category are still growing. What is collapsing is specifically the liquidity
deposit — the ordinary account. The money is largely moving to time deposits, JGBs and insurance,
which is a rate story rather than a risk-appetite story. Long-term lending rates crossed 2% in
June for the first time in 25 years.

Also worth noting: equities and investment trusts together took in ¥1.5tn while investment trusts
alone took in ¥3.0tn — so households are buying funds and net selling individual shares.

And seasonally adjusted, households went to a net financial deficit (−¥1.3tn from +¥4.9tn).
Dai-ichi Life is cautious about reading much into it since the adjusted series swings hard, but
it's an unusual print for a sector that has been in surplus for decades.

Sources: BOJ flow of funds Q1 2026, with the reads from Dai-ichi Life Research Institute and NLI
Research Institute.
```

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

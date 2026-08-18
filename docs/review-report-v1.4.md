# v1.4.0 Chinese homepage voice review

Review date: **2026-08-18**

Scope: Chinese copy and bilingual information structure in `README.md` only. The detailed Chinese SOP, matrix, manager add-on, quick card, and scenarios were intentionally left unchanged.

This is an editorial self-audit, not independent user research.

## 1. Problem

The homepage often placed an English sentence and a matching Chinese sentence on the same line or under the same bilingual heading.

Even when the meaning was correct, the Chinese inherited English abstractions and rhythm. Phrases such as “传递一个简短信号,” “自愿才算自愿,” and “最小闭环” sounded more like translated training copy than a Chinese colleague speaking.

The goal was not to make the copy casual at any cost. It was to sound current, direct, and human while keeping privacy, power, consent, and escalation rules intact.

## 2. Editorial decision

**Decision:** separate the languages before rewriting the Chinese.

The homepage now has an English track and a Chinese entry section, English and Chinese exercise groups, two independently written loops, and separate safety lists.

Chinese follows this voice:

- start from a recognizable workplace moment;
- use short sentences and concrete verbs;
- say what to do next before explaining the framework;
- allow “别硬聊,” “别追问,” and “就到这里” when they sound natural;
- avoid short-lived memes, “i 人/e 人” labels, or exaggerated internet slang;
- keep formal terms only where harassment, reporting, accessibility, or legal meaning requires them.

## 3. Before and after

| Before | After | Why |
| --- | --- | --- |
| “寒暄不是表演，也不是套隐私。它只传递一个简短信号……” | “寒暄没那么玄。碰见了就打个招呼，聊得来多说两句，接不上也别硬撑。” | Replaces an abstract definition with a familiar moment and an action |
| “自愿才算自愿” | “对方不接，就到这里” | Gives the reader a usable stop rule |
| “互惠，不审问” | “别只顾着问。问一两句，也说点自己” | Sounds spoken and explains the behavior |
| “没有绝对安全的话题” | “别觉得聊周末、吃饭、家里就肯定没事” | Replaces an abstract label with recognizable topics and a direct caution |
| “最小闭环” | “中文版：看—开—接—收” under an independent section | Removes product-language framing from the Chinese path |
| English and Chinese on every safety line | Two separate seven-item lists | Lets each language choose its own sentence shape |

## 4. Review loop

| Pass | Lens | Finding | Revision |
| --- | --- | --- | --- |
| 1 | Structure | Paired headings made Chinese feel like subtitles | Removed inline bilingual H2 and H3 headings |
| 2 | Entry copy | The route table translated the same intent row by row | Replaced it with separate English and Chinese paths |
| 3 | Spoken rhythm | Chinese relied on abstract nouns and balanced slogans | Rewrote around actions, short clauses, and familiar situations |
| 4 | Durability | “Young internet style” could drift into memes | Kept conversational words but rejected disposable slang |
| 5 | Safety regression | Looser wording could weaken boundaries | Rechecked opt-out, power, privacy, identity, repair, and escalation meaning |
| 6 | Interaction | English and Chinese exercises became interleaved | Grouped both English examples before both Chinese examples |
| 7 | GitHub rendering | New headings could break the top practice link | Updated the anchor and reran GitHub Markdown rendering |

## 5. Acceptance tests

| # | Test | Result |
| ---: | --- | --- |
| 1 | Chinese hero line reads naturally without the English sentence | Pass |
| 2 | No Markdown H2 or H3 pairs English and Chinese with an inline slash | Pass |
| 3 | English and Chinese navigation paths are independent | Pass |
| 4 | English exercises and Chinese exercises are grouped separately | Pass |
| 5 | The two safety lists are independently written | Pass |
| 6 | The user-flagged “传递一个简短信号” sentence is gone | Pass |
| 7 | Flagged translationese phrases are absent from the README | Pass |
| 8 | No “i 人/e 人,” meme, or short-lived platform slang was introduced | Pass |
| 9 | Short answers and disengagement still route to a prompt exit | Pass |
| 10 | Manager power, privacy, identity, and non-retaliation meaning remains | Pass |
| 11 | Harassment, discrimination, coercion, retaliation, and threats still route to formal support | Pass |
| 12 | Four `<details>` examples and the practice anchor survive GitHub rendering | Pass |

Result: **12/12 passed**.

## 6. Score

| Criterion | Weight | Score | Reason |
| --- | ---: | ---: | --- |
| Native Chinese voice | 25 | 24 | Concrete and conversational without becoming flippant |
| Bilingual structure | 20 | 20 | Languages now have separate paths, exercises, and safety lists |
| Meaning preservation | 20 | 20 | Consent, power, privacy, identity, and escalation remain intact |
| Scanability | 15 | 15 | Short entry lists and language-specific subheadings |
| Durability | 10 | 9 | Avoids memes; contemporary phrasing will still need periodic review |
| Maintainability | 10 | 9 | Contribution rules and automated regression phrases added |
| **Total** | **100** | **97** | Pass |

## 7. Limitations

- Chinese tone varies by age, city, industry, and company. “Natural” is not universal.
- The rewrite was not tested with a formal sample of young Chinese employees.
- Some safety and escalation language remains formal because precision matters more than casual tone there.
- The homepage is still bilingual; readers who want a fully Chinese flow should use the dedicated Chinese documents.

Watch for feedback that a phrase feels too corporate, too online, too northern or southern, too formal for peers, or too casual across hierarchy.

## 8. Final decision

**Pass v1.4.0 for inclusion, subject to local checks and GitHub Actions on the published commit.**

The homepage now behaves like two related guides sharing one front door, not an English page with Chinese subtitles.

If future edits restore sentence-by-sentence pairing, abstract translationese, or disposable internet slang, stop release and rerun all 12 tests after revision.

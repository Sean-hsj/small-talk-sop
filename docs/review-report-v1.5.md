# v1.5.0 Chinese homepage tone review

Review date: **2026-08-18**

Scope: Chinese copy in `README.md`, the adjacent English hero line, and the rules and automated checks needed to keep that voice stable. The English guide and all files under `docs/zh-CN` were left unchanged.

This review responds to direct reader feedback that the v1.4 homepage still sounded paternalistic. It is an editorial self-audit, not a broad user study.

## 1. Problem

The sentence “不教你‘会来事’，只帮你把第一句、下一句和最后一句说自然” defined the reader by a presumed weakness, then positioned the guide as the authority correcting it.

Similar patterns remained elsewhere: “先别急着看答案,” “先记住这七句,” and “不用从头背到尾.” Each line was understandable, but together they made the page sound like a lesson delivered from above.

## 2. Editorial standard

Homepage copy should treat readers as capable adults choosing a reference tool.

- Introductions state what the repository is.
- Navigation states what each link contains.
- Examples describe the situation and the reasoning.
- Frameworks name the steps without narrating the reader's behavior.
- Direct instructions remain only where a boundary needs to be unmistakable.
- Slogans do not replace information.

## 3. Review loop

| Pass | Area | Finding | Revision |
| --- | --- | --- | --- |
| 1 | Hero | The “不教你……只帮你……” contrast sounded corrective and self-important | Replaced it with a one-sentence description of the bilingual guide |
| 2 | Intro callout | “寒暄没那么玄” answered an objection the reader had not made | Replaced it with a factual summary of the repository's coverage |
| 3 | Chinese navigation | Every link told the reader what to do or assumed they were stuck | Recast the list as a resource directory |
| 4 | Exercises | “先别急着看答案” reproduced a classroom voice | Described how the expandable examples work |
| 5 | Four-step loop | Repeated commands made a neutral framework sound disciplinary | Rewrote the steps as short descriptions |
| 6 | Safety | Removing all imperatives could weaken consent and power boundaries | Kept the meaning, while changing most rules into factual observations |
| 7 | Usage | “先读” and “别把” placed the page above the reader | Recast the section as available ways to use the material |
| 8 | Footer | The closing slogan added another polished instruction | Removed it |

## 4. Before and after

| Before | After | Reason |
| --- | --- | --- |
| “不教你‘会来事’，只帮你……” | “一份中英双语职场寒暄指南。” | States what the project is without diagnosing the reader |
| “寒暄没那么玄” | “这里整理了职场里常见的开场、接话和收尾……” | Replaces reassurance from above with a content description |
| “第一次看，先从……” | Link title followed by a description | Lets readers choose their own route |
| “先别急着看答案” | “下面是两个可以直接展开的场景” | Explains the interaction without classroom language |
| “中文版先记住这七句” | “中文版：七条边界” | Names the section without issuing a command |
| “中文读者不用从头背到尾” | “中文版各章节可以单独阅读” | Describes the document structure without imagining a mistake |

## 5. Acceptance tests

| # | Test | Result |
| ---: | --- | --- |
| 1 | Hero Chinese is a direct, declarative description | Pass |
| 2 | Hero does not use “不……只……” contrast framing | Pass |
| 3 | Adjacent English hero line also describes the guide without diagnosing readers | Pass |
| 4 | Intro callout describes content rather than correcting an attitude | Pass |
| 5 | Chinese navigation is a resource directory, not a sequence of commands | Pass |
| 6 | Exercise introduction contains no teacher-like pacing instruction | Pass |
| 7 | Four-step loop remains understandable after unnecessary commands are removed | Pass |
| 8 | Safety section no longer says “先记住” | Pass |
| 9 | Consent, power, privacy, identity, repair, and escalation meanings remain | Pass |
| 10 | Usage section offers formats without turning the SOP into an authority | Pass |
| 11 | Closing Chinese slogan is removed | Pass |
| 12 | Four expandable examples remain and detailed Chinese documents are unchanged | Pass |

Result: **12/12 passed**.

## 6. Score

| Criterion | Weight | Score | Reason |
| --- | ---: | ---: | --- |
| Equal-footing tone | 30 | 29 | Reader deficiency and top-down lesson framing removed |
| Clarity | 20 | 20 | Hero and navigation now state their purpose directly |
| Meaning preservation | 20 | 20 | Safety boundaries remain explicit |
| Natural Chinese | 15 | 14 | Less slogan-like; regional and age variation still exists |
| Maintainability | 10 | 9 | Contribution rules and regression phrases added |
| Validation depth | 5 | 4 | Direct feedback addressed, but no wider reader panel |
| **Total** | **100** | **96** | Pass |

## 7. Limitations

- This pass addresses one reader's specific and persuasive feedback; it does not establish a universal Chinese voice.
- Safety language is intentionally firmer than navigation and descriptive copy.
- The rest of the English homepage was outside this tone review.

## 8. Final decision

**Pass v1.5.0 for release after local checks, GitHub rendering, and main-branch CI succeed.**

Future homepage edits should be rejected if they diagnose the reader before offering help, manufacture a contrast for rhetorical effect, turn navigation into instruction, or replace a plain description with a slogan.

# v1.0.0 research and review report

- Review date: 2026-08-18
- Reviewed branch: agent/workplace-small-talk-sop
- Source commit: recorded as the draft pull request head SHA; a Git commit cannot embed its own final hash
- Final decision: **Pass — recommend release at 97/100 safety review**
- Conservative release floor: **95/100**, the lowest final locale or safety score

This report records the actual review loop. The reviewer roles were independent AI-agent simulations with shared access to the repository, not a substitute for named human employees, lawyers, clinicians, accessibility specialists, or representatives of every culture described.

## 1. Review roles

1. International and multinational workplace researcher: English naturalness, North American, UK/Irish, Australian/New Zealand, European, global-English, remote, and second-language use
2. Chinese workplace-culture researcher: titles, hierarchy, indirect refusals, meals, alcohol, WeChat and enterprise chat, industry, generation, region, and natural Mandarin
3. HR, DEI, privacy, accessibility, and compliance red team: consent, power, harassment, retaliation, identity, disability, neurodiversity, alcohol, health, family, remote work, and escalation
4. Primary editor: information architecture, bilingual divergence, consistency, source register, automated checks, issue resolution, and release decision

The review used the process and rubric in [review-loop.md](review-loop.md).

## 2. Round 1 — research and architecture

Three independent research tracks supplied:

- executable opening, continuation, signal-reading, exit, boundary, and repair patterns;
- separate cultural defaults for international English and mainland-China Chinese workplaces;
- legal and policy anchors plus peer-reviewed, university, government, accessibility, and professional sources;
- scenario matrices and acceptance checklists.

The first draft separated each locale into a full SOP, one-minute card, and scenario set. Shared safety rules, cross-cultural adaptation, evidence, contribution rules, and the recurring review loop were kept outside either locale so one version would not become a translation master.

## 3. Round 2 — red-team result: No-Go

| Reviewer | Score | Gates / tests | Decision |
| --- | ---: | --- | --- |
| English workplace and naturalness | 91/100 | 8/8 gates | Conditional pass |
| Chinese workplace and naturalness | 90/100 | 8/8 gates | Conditional pass |
| HR / DEI / privacy / compliance | 93/100 | 8/8 gates; 42/44 stress points | **No-Go** |

The numerical threshold was met, but publication was paused because:

1. photography, recording, posting, forwarding, and tagging lacked a separate-consent rule;
2. a declined, ignored, redirected, or vaguely postponed personal invitation did not have an explicit one-attempt rule;
3. several English and Chinese scripts sounded like training or therapy language rather than ordinary workplace speech;
4. AAC and speech-disabled participation were only implicit;
5. non-desk, shift, factory, laboratory, service, healthcare, hospitality, retail, and logistics examples were too thin;
6. appearance-comment alternatives could still infer workload or health from appearance;
7. the release record did not yet contain verifiable scores and tests.

## 4. Revision between rounds

The editor:

- added separate consent before taking, recording, posting, forwarding, or tagging workplace photos and video;
- stated that attendance or appearing in frame is not publication consent and added private, non-punitive group-photo opt-outs;
- limited personal invitations to one attempt and treated a decline, silence, topic change, or vague delay as closure;
- prohibited channel-switching, reason-seeking, work retaliation, and manager-to-direct-report romantic invitations;
- added AAC, typing, interpreter, processing-time, and direct-address guidance and a practice scenario;
- added factory, laboratory, field, shift, retail, hospitality, healthcare, logistics, and customer-facing guidance;
- removed the extra OAR and EAR mnemonics, leaving SAFE as the single English memory model;
- replaced training-style or translated language in both locales;
- changed the Chinese leader-elevator scene from praise to an ordinary greeting;
- changed late-night manager messaging to draft or scheduled delivery during work time;
- separated ordinary-colleague and duty-bearing responses to domestic-violence or safety disclosure;
- clarified titles such as 师傅, 某工, and formal office titles without making them universal;
- separated private financial or belief interrogation from lawful, voluntary discussion of pay and working conditions;
- added Canadian and New Zealand official safety sources and clarified that regional English notes are editorial hypotheses.

## 5. Round 3 — final independent scores

| Criterion | Weight | English review | Chinese review | HR safety review |
| --- | ---: | ---: | ---: | ---: |
| Executability | 15 | 15 | 15 | 15 |
| Natural language | 15 | 14 | 13 | 14 |
| Cultural fit and humility | 15 | 14 | 14 | 14 |
| Consent, privacy, and power | 20 | 20 | 20 | 20 |
| Inclusion and accessibility | 15 | 15 | 15 | 15 |
| Scenario coverage | 10 | 10 | 10 | 10 |
| Evidence and maintainability | 10 | 9 | 8 | 9 |
| **Total** | **100** | **97** | **95** | **97** |

All three final reviews exceeded 90/100, and no criterion scored below 70% of its weight.

## 6. Critical safety gates

| Gate | Result |
| --- | --- |
| No coercion, retaliation, outing, identity-based humor, or repeated intrusive questions | Pass |
| Managers and other high-power roles follow stricter rules than peers | Pass |
| A recipient can leave or decline without explaining | Pass |
| No assumptions about gender, partner, family, disability, religion, nationality, age, diet, or alcohol | Pass |
| Private disclosure is not repeated, posted, tagged, or repurposed without permission | Pass |
| Serious conduct routes to policy and support without requiring personal confrontation first | Pass |
| Digital channels, clients, travel, events, physical contact, bystander action, and retaliation are covered | Pass |
| The SOP cannot be used to suppress protected discussion of pay, hours, conditions, or organizing | Pass |

Result: **8/8 Pass**.

## 7. Adversarial stress test

Each test scored 0–2: 2 means the SOP handles the boundary, power/privacy dimension, and next step; 1 means partial handling; 0 means continued pressure, justification, propagation, or punishment.

| # | Scenario | Score |
| ---: | --- | ---: |
| 1 | Manager asks a junior employee about dating | 2 |
| 2 | Leader pressures drinking at a Chinese business meal | 2 |
| 3 | Senior colleague repeats or moves a declined invitation to another channel | 2 |
| 4 | Colleague imitates an accent | 2 |
| 5 | Colleague mentions a same-gender partner | 2 |
| 6 | Name or pronoun is corrected | 2 |
| 7 | Health or mental-health information is disclosed | 2 |
| 8 | Pregnancy or body is inferred or commented on | 2 |
| 9 | Fasting, prayer, or religious diet is involved | 2 |
| 10 | Client or team pressures political participation | 2 |
| 11 | Neurodivergent colleague does not make eye contact | 2 |
| 12 | Someone touches or moves a wheelchair or assistive device | 2 |
| 13 | Handshake, hug, or step-back signal is mishandled | 2 |
| 14 | Video background, home, or family appears on camera | 2 |
| 15 | Manager sends an after-hours message and expects instant response | 2 |
| 16 | Client makes an identity-based or sexual joke | 2 |
| 17 | Employees voluntarily discuss pay or working conditions | 2 |
| 18 | “下次吧” or another indirect refusal is ignored | 2 |
| 19 | Work-event photo is recorded, published, forwarded, or tagged without separate permission | 2 |
| 20 | Initiator repairs an intrusive question | 2 |
| 21 | Second-language speaker misses sarcasm or slang | 2 |
| 22 | Domestic violence or immediate safety risk is disclosed | 2 |

Result: **44/44 Pass**. No critical scenario scored zero.

## 8. Validation

The reviewed content snapshot produced:

> Documentation checks passed: 11 Markdown files, 11 required files.

After adding this review record to the release package, the check is expected to report 12 Markdown files and 12 required files and must be rerun before commit. The check covers:

- required artifacts;
- internal Markdown targets and anchors;
- unresolved placeholders;
- required release markers;
- whitespace errors through git diff checking.

It does not validate external availability, legal currency, or whether a source still supports a claim.

### External links

The final pre-release HTTP pass found **43 unique external links**:

- 30 returned HTTP 200;
- 8 returned HTTP 403 from publisher or official-site access controls;
- 5 timed out;
- 0 returned HTTP 404 or 410.

The restricted items were manually reviewed by canonical DOI, official domain, prior successful response, or focused browser/search verification. The Canada official page had returned HTTP 200 in the prior pass. The NLRB wage-discussion page was verified through the official-domain search result and summary. British Council pages, ILO NORMLEX, academic publishers, the Australian Human Rights Commission, University of Minnesota, and CDC may restrict automated requests. This is not proof that every URL will remain available; [SOURCES.md](../SOURCES.md) requires annual and change-triggered human review.

## 9. Known limitations

- Reviewer roles were simulated; the project still needs feedback from real workers in additional regions, languages, power levels, and accessibility contexts.
- Manufacturing, healthcare, logistics, hospitality, retail, education, government, public institutions, and state-owned-enterprise environments need more field examples despite being represented.
- Country and region notes are cautious hypotheses, not representative samples.
- The repository is guidance, not a legal determination, medical protocol, crisis service, or substitute for company policy and collective agreements.
- Platform behavior and workplace law can change faster than core conversation principles.

## 10. Final decision

**Pass v1.0.0.** Release is authorized after the dependency-free documentation check and whitespace check pass, the branch is pushed, the GitHub Actions check is green, and the draft pull request records its exact head SHA.

# v1.1.0 role and scenario refinement review

- Review date: 2026-08-18
- Scope: role, reporting line, gender/identity, age/life stage, occasion, meal size, and meal purpose
- Final score: **97/100**
- Final decision: **Pass — recommend updating the existing draft PR**

This refinement was reviewed by the primary editor through structured role simulation. It did not repeat the independent multi-agent review used for v1.0.0.

## 1. Requested coverage

### Role coverage

| Requested dimension | English matrix | Chinese matrix |
| --- | --- | --- |
| Peer | Same-team, cross-team, new or less-established peer | 同团队、跨部门、新人或资历较浅同级 |
| Direct report | Power-aware direct-report playbook | 下属与领导可信退出规则 |
| Direct manager | Manager playbook and one-to-one lunch | 直属上级与单独午饭 |
| Manager +1/+2 | Senior-level brief contact and meal rules | 加一、加二、高层与越级午饭 |
| Vice/deputy manager | Deputy, assistant, vice, dotted-line, matrix distinctions | 副职、副经理、矩阵与虚线上级 |
| Mentor or sponsor | Developmental relationship limits | 带教、导师与 sponsor |

### Occasion coverage

Both matrices cover:

- Monday and return from a weekend;
- public holiday and vacation return;
- return from unexplained leave;
- buying coffee;
- before and after lunch;
- a casual break;
- before and after a meeting;
- deadline, shift end, and remote Monday.

### Meal coverage

Both matrices distinguish:

- one-to-one peer lunch;
- two or three colleagues;
- a larger social lunch;
- lunch meeting;
- manager and employee one-to-one;
- skip-level lunch;
- client or vendor meal;
- team dinner with alcohol.

## 2. Segmentation safety rule

The new material does not assign topics by gender or guessed age.

The decision order is:

1. power;
2. setting;
3. purpose;
4. group size;
5. voluntarily disclosed context.

Gender, partner, marriage, children, pregnancy, caregiving, living arrangement, and retirement appear only as volunteered context.

## 3. Gender and identity review

The matrices passed these checks:

- same baseline boundaries across genders;
- no identity inference from appearance, voice, clothing, body, or partner;
- volunteered names, pronouns, and relationship terms are mirrored;
- no appearance-based routine compliments;
- mentoring and career access remain equal across genders;
- transparency is used instead of excluding a gender for “optics”;
- one invitation and any non-acceptance ends the topic;
- private or enclosed settings increase safeguards for everyone.

## 4. Age and life-stage review

The matrices passed these checks:

- no age bracket receives a personality script;
- early-career status does not justify infantilizing language;
- older colleagues are not presumed unhealthy, retiring, or unable to use technology;
- similar age does not create automatic intimacy;
- a mentioned child opens only one proportional follow-up;
- marriage, fertility, school cost, grades, custody, and parenting choices remain closed;
- pregnancy and parental leave are never inferred;
- caregiving disclosure moves to work support only when relevant to the listener’s role.

Two additional official age-discrimination sources were added and returned HTTP 200 during review.

## 5. Meal and group-size review

The refinement separates group size from meal purpose.

A one-to-one meal may create privacy or romantic ambiguity. A larger meal may create forced disclosure, exclusion, or status clustering.

A lunch meeting remains a meeting. It needs an agenda, accessibility, official decisions, and work-time treatment where policy requires.

Manager meals state whether they are casual, developmental, or performance-related. A direct report can decline without losing information or opportunity.

Two- or three-person meals include an anti-inside-circle rule. Group meals keep important decisions in official channels.

## 6. Adversarial refinement tests

| # | Test | Result |
| ---: | --- | --- |
| 1 | Peer gives a broad Monday answer | Pass |
| 2 | A colleague mentions a child once | Pass |
| 3 | Manager lunch introduces surprise feedback | Pass |
| 4 | Direct report declines lunch | Pass |
| 5 | Manager +2 is met in a coffee queue | Pass |
| 6 | Deputy and matrix instructions conflict | Pass |
| 7 | Three-person lunch becomes a two-person inside story | Pass |
| 8 | Older colleague is stereotyped around technology | Pass |
| 9 | Cross-gender mentoring is withheld for “optics” | Pass |
| 10 | Return-from-leave reason is unknown | Pass |
| 11 | Pregnancy is visible but not disclosed | Pass |
| 12 | Partner term is volunteered | Pass |
| 13 | Mandatory work is called a social lunch | Pass |
| 14 | Manager uses small talk to test after-hours availability | Pass |
| 15 | Skip-level meal invites criticism of the direct manager | Pass |
| 16 | Team dinner makes alcohol or staying late feel required | Pass |

Result: **16/16 Pass**.

## 7. Score

| Criterion | Weight | Score |
| --- | ---: | ---: |
| Executability | 15 | 15 |
| Natural language | 15 | 14 |
| Cultural fit and humility | 15 | 15 |
| Consent, privacy, and power | 20 | 20 |
| Inclusion and accessibility | 15 | 15 |
| Scenario coverage | 10 | 10 |
| Evidence and maintainability | 10 | 8 |
| **Total** | **100** | **97** |

No criterion is below 70% of its weight. All v1.0 critical safety gates remain applicable and pass.

## 8. Known limitations

- The refinement is a decision matrix, not a statistical model of workplace behavior.
- Family and life-stage examples still need field feedback from more cultures and industries.
- “Vice manager,” “加一,” “加二,” and matrix titles vary by organization.
- Meal cost, work time, alcohol, reporting-line, and relationship policies vary.
- The guide cannot determine another person’s identity or consent from demographic labels.

## 9. Final decision

**Pass v1.1.0.** Add the refinement as a new commit to the existing draft PR after local documentation and whitespace checks pass, then require remote GitHub Actions to pass again.

# Research, review, and improvement loop

This document turns “keep improving it” into a repeatable quality system. It applies to releases and to individual contributions.

## Definition of done

A release is acceptable only when it:

- gives an executable beginning, middle, and ending—not just topic lists;
- provides natural scripts in the target language;
- separates shared safety rules from locale-specific defaults;
- covers in-person, remote, group, hierarchy, meal, newcomer, and recovery scenarios;
- protects voluntary participation, privacy, dignity, and work access;
- includes usable alternatives for every major “do not”;
- supports second-language speakers, introverts, neurodivergent people, disabled colleagues, and people with limited social energy;
- labels generalizations and cites material research or policy claims;
- passes every critical safety gate and scores at least 90/100 below.

## The loop

### 1. Discover

Collect scenarios from the target environment and current reliable sources. Separate:

- evidence-backed findings;
- official legal or policy guidance;
- widely observed practice;
- organization-specific convention;
- individual preference.

Never convert one anecdote into a national norm.

### 2. Draft

For each recommendation write:

- the situation;
- the goal;
- the safest default action;
- one or more phrases people can actually say;
- a stop signal;
- a clean exit;
- a culture, power, accessibility, or privacy caveat where relevant.

### 3. Role review

Run the draft through at least these perspectives:

1. New hire who knows nobody
2. Second-language English or Mandarin speaker
3. Introverted or socially anxious employee
4. Autistic, ADHD, hard-of-hearing, speech-disabled, or low-energy colleague
5. Junior employee speaking with a manager
6. Manager whose friendliness carries implicit pressure
7. Colleague from a marginalized identity who is often asked to explain it
8. Remote worker who misses hallway context
9. Local colleague who finds imported corporate language unnatural
10. HR or people-risk reviewer

Reviewers ask: “Could I decline without cost? Could this expose private information? Would this phrase sound normal when spoken? What happens after a short answer?”

### 4. Adversarial scenario test

At minimum, test:

- the person has headphones on or is rushing;
- the person replies with one word and asks nothing back;
- a manager asks a junior employee about dating, pregnancy, religion, health, or weekend availability;
- someone discloses grief, illness, discrimination, or financial stress;
- a colleague starts gossiping about an absent coworker;
- a joke lands badly;
- a name or pronoun is used incorrectly;
- a meal includes alcohol pressure or dietary assumptions;
- a group-chat comment exposes a private one-to-one detail;
- a direct English script feels cold in Chinese, or an indirect Chinese script becomes unclear in a multinational team;
- the employee cannot or does not want to make eye contact, speak quickly, attend social events, or process noisy spaces;
- the conversation could be mistaken for flirting, performance feedback, or an off-the-record work request.
- a personal invitation is declined, ignored, redirected, or vaguely postponed, then moved to another channel;
- an organizer photographs, records, posts, forwards, or tags people from a work event without separate permission.

The guidance must either handle the case or explicitly route the reader to company policy or professional support.

### 5. Score

| Criterion | Weight | Full-credit question |
| --- | ---: | --- |
| Executability | 15 | Can a nervous reader choose a moment, say one line, respond, and leave? |
| Natural language | 15 | Would fluent colleagues in the target environment actually say these phrases? |
| Cultural fit and humility | 15 | Are local defaults useful, qualified, and free of national stereotypes? |
| Consent, privacy, and power | 20 | Is participation genuinely optional even across hierarchy? |
| Inclusion and accessibility | 15 | Can different identities, abilities, language levels, and energy levels use or decline it? |
| Scenario coverage | 10 | Are common channels and failure modes covered? |
| Evidence and maintainability | 10 | Are material claims sourced, dated, linkable, and easy to update? |

Passing score: **90/100**. No criterion may score below 70% of its weight.

### 6. Critical safety gates

Any “no” blocks release regardless of the numerical score:

- Does the SOP clearly prohibit coercion, retaliation, outing, discriminatory humor, and repeated intrusive questions?
- Do managers receive stricter rules than peers?
- Can the recipient exit without explaining why?
- Does the SOP avoid assuming gender, partner, family, disability, religion, nationality, age, diet, or alcohol use?
- Does it tell readers not to repeat private disclosures?
- Does serious misconduct route to policy/support instead of requiring personal confrontation?
- Does the guidance cover digital channels, clients, work travel, social events, physical contact, bystander action, and retaliation?
- Does it avoid being used to suppress legally protected discussion of pay, hours, working conditions, or organizing?

### 7. Revise and log

Fix high-severity failures first, then naturalness and coverage. Re-run only the affected tests plus all critical gates. Record:

- date and version;
- reviewers or simulated perspectives;
- scenarios tested;
- material changes;
- unresolved limitations;
- score and gate result.

### 8. Release and monitor

After release, watch issues and pull requests for recurring confusion, cultural drift, dead sources, or examples that age badly. Review annually at minimum. Earlier review is required after material legal changes, major workplace-channel changes, or repeated reports of harm.

The automated documentation check verifies required files, internal links and anchors, unresolved placeholders, and a few release markers. It does **not** prove that an external URL is reachable, a source still supports a claim, or legal guidance remains current. External sources and legal content require the dated human review recorded in the source register and release record.

## Release review record: v1.0.0

| Pass | Focus | Result |
| --- | --- | --- |
| 1 | Coverage and information architecture | Separate locale SOPs, quick cards, scenarios, cultural notes, and sources required |
| 2 | International and Chinese workplace naturalness | Translation symmetry rejected; titles, indirect exits, meals, group chat, remote work, and hierarchy localized |
| 3 | HR, inclusion, privacy, and power | Manager power multiplier, opt-out signals, privacy boundary, identity assumptions, accessibility, and escalation added |
| 4 | Adversarial script test | Short replies, awkward silence, grief, gossip, alcohol, misnaming, intrusive questions, remote messages, and unwanted flirting handled |

The final numerical scores, gate results, stress tests, validation output, external-link audit, changes between review rounds, and limitations are recorded in the [v1.0.0 review report](review-report-v1.0.md). Future releases must add their own record rather than overwriting this one.

## Refinement review record: v1.1.0

The role, reporting-line, occasion, meal-size, gender/identity, age, and voluntarily disclosed life-stage refinement is recorded in the [v1.1.0 review report](review-report-v1.1.md). It supplements rather than overwrites the v1.0.0 record.

## Add-on review record: v1.2.0

The optional manager communication-style model, bilingual scripts, rejection of fixed personality types, audit rounds, 14 adversarial tests, and 10 release gates are recorded in the [v1.2.0 review report](review-report-v1.2.md).

Any future change to the add-on must rerun all 10 add-on gates. A diagnosis, identity stereotype, appeasement tactic, abuse-as-style exception, or missing preference-check loop blocks release.

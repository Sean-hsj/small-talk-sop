# Contributing

Contributions are welcome, especially from people working in environments not yet represented. The goal is safer, more natural workplace interaction—not one universal personality standard.

## What makes a useful contribution

- A real workplace situation the current SOP does not handle
- A phrase that sounds unnatural, dated, too intimate, overly formal, or culturally misplaced
- A boundary or accessibility problem
- A regional, industry, role, remote-work, or hierarchy exception
- A reliable source that changes or qualifies a recommendation
- A tested improvement to the review process

Do not submit identifiable stories, private workplace messages, names, screenshots, employer secrets, or personal data. Generalize examples and obtain consent before quoting anyone.

## Required change note

Every pull request that changes guidance should state:

1. Which locale and scenario it affects
2. What could go wrong with the current wording
3. Who may be helped or harmed by the change
4. Whether the suggestion is evidence, common practice, or personal experience
5. Which scenario tests were run
6. Whether the English and Chinese guides should intentionally diverge

## Review path

1. **Author pass:** check clarity, naturalness, opt-out language, and links.
2. **Locale pass:** a fluent speaker familiar with the target workplace checks whether the phrase would actually be said.
3. **Power and inclusion pass:** review from junior employee, manager, marginalized colleague, neurodivergent colleague, and second-language speaker perspectives.
4. **Adversarial scenario pass:** test awkward timing, short answers, sensitive disclosures, gossip, alcohol pressure, and cross-cultural misunderstanding.
5. **Maintenance pass:** confirm no universal claim is presented as a national rule and update the source register if evidence changed.

Use the scoring rubric and release gate in [docs/review-loop.md](docs/review-loop.md). A change that fails consent, privacy, power-safety, or anti-harassment is blocked even if its total score is high.

## Style

- Write scripts people can say aloud in one breath.
- Prefer concrete verbs and short sentences.
- Give a safe alternative, not only a prohibition.
- Label regional and organizational variation.
- Separate observation from stereotype: “This team uses first names” is useful; “Americans are informal” is too broad.
- Translate meaning only when appropriate. Do not force one-to-one symmetry between the two guides.
- On bilingual landing pages, give each language its own paragraph or section. Do not attach a Chinese translation to every English heading or sentence.
- Write Chinese from the situation outward: who is speaking, what happened, and what to do next. Prefer concrete verbs such as “别追问” over abstract labels such as “降低互动强度.”
- Contemporary is good; disposable slang is not. Avoid wording that depends on “i 人/e 人,” memes, or short-lived platform language.
- Address readers as capable adults. Use neutral descriptions for introductions, navigation, and examples; avoid “不教你……只帮你……,” “先记住……,” or other language that invents a reader deficiency before offering help.
- Use direct instructions sparingly. They belong in consent, privacy, harassment, or safety boundaries—not in slogans or routine navigation.

## Visual and interaction contributions

- Keep every rule and script available as text. An image may support memory, but it must not carry required information alone.
- Add concise, action-based alt text at every image use. Localize meaning naturally instead of translating alt text mechanically.
- Follow the [illustration system](assets/illustrations/README.md): black pen-and-ink, pure white, sparse cobalt accents, and ordinary workplace gestures.
- Avoid identity stereotypes, sexualization, authority worship, compulsory bonding, stock characters, decorative clutter, embedded text, and visual jokes that weaken consent.
- Keep each raster below 1.2 MB. Add a new, descriptive filename instead of silently overwriting an approved asset.
- Use GitHub-native links, callouts, tables, and `<details>` for interaction. Do not require scripts, tracking, animation, pointer-only gestures, or separate hosting.
- If an asset is generated or substantially transformed by a tool, record the prompt set, production date, selection or editing steps, and limitations in the asset notes.
- Rerun the visual gates in the [v1.3 review report](docs/review-report-v1.3.md) and the repository checker before publishing.

## Versioning

- Patch: wording, link, or example correction with no behavioral change
- Minor: new scenario, locale note, or recommendation
- Major: changes to the core operating model or safety rules

Substantive guidance should be re-reviewed at least annually, and sooner after material legal, workplace-policy, or cultural changes.

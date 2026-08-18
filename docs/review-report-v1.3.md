# v1.3.0 visual design and interaction review

Review date: **2026-08-18**

Scope: visual hierarchy, project illustrations, native GitHub Markdown interaction, navigation, accessibility, and asset performance. The v1.2 safety and content model remains unchanged.

This is an editorial and technical self-audit, not independent accessibility certification or user research.

## 1. Design decision

**Decision:** add a small, consistent illustration system and GitHub-native interaction. Do not turn the repository into a separate website.

The chosen direction is black editorial pen-and-ink on pure white, with one restrained cobalt-blue accent. It uses ordinary workplace gestures, open space, and a slightly dry single-panel-comic tone.

The following directions were rejected:

- beige, cream, pastel, or atmospheric backgrounds;
- gradients, glossy 3D, soft clay, airbrush, or cinematic lighting;
- corporate-vector people, floating shapes, oversized heads, or exaggerated smiles;
- text baked into generated images;
- decorative images that repeat on every page;
- scripts, animation, or interaction requiring separate hosting;
- novelty that weakens privacy, power, consent, or accessibility guidance.

## 2. Review loop

| Pass | Lens | Finding | Revision |
| --- | --- | --- | --- |
| 1 | Art direction | A generic “friendly office” prompt could drift into stock or generated-image clichés | Fixed black ink, pure white, cobalt accents, sparse props, and a detailed avoid list |
| 2 | Scene meaning | A greeting image could imply that stopping is required | Kept the walking path open and showed a brief wave rather than a blocking conversation |
| 3 | Power and groups | Manager and lunch scenes could reinforce authority or compulsory bonding | Used equal seated dignity, calm preference checking, an open door, and an unchallenged exit |
| 4 | Information access | Instructions inside art would fail when images are hidden or unreadable | Removed all words and kept every instruction in Markdown text |
| 5 | GitHub interaction | Custom controls would not be reliable in repository Markdown | Used native headings, links, tables, callouts, and four `<details>` exercises |
| 6 | Theme and performance | Transparent black lines can disappear in dark mode; original PNGs were heavier | Retained a white comic panel and resized assets to 1,500–1,600 pixels |
| 7 | Maintainability | New art could drift in style or lose alt text | Added a versioned asset guide, approved alt text, prompt set, and automated file gates |

Affected pages and all visual gates were rechecked after each revision.

## 3. Asset review

| Asset | Intended meaning | Result |
| --- | --- | --- |
| `coffee-hello.png` | Brief recognition plus an unobstructed exit | Pass |
| `manager-calibration.png` | Try a format, inspect detail, and agree a next step | Pass |
| `lunch-easy-exit.png` | Group warmth without pressure to stay | Pass |

All three final files have:

- no embedded words, labels, logos, or watermarks;
- high-contrast black line work on pure white;
- cobalt blue used only as a spot accent;
- ordinary contemporary clothing and non-sexualized bodies;
- readable actions after reduction to GitHub content width;
- localized, action-based alt text at every point of use.

No factual rule exists only in an image. The art may be skipped without losing the SOP.

## 4. Interaction review

The README adds four collapsed practice scenes. Each summary contains the situation and decision prompt. Expanding reveals one safer line and the principle behind it.

The exercises use native `<details>` and `<summary>` elements. They require no JavaScript, account, tracking, form submission, animation, or remote state.

The main routes remain ordinary links. A reader can skip the interactive examples and go directly to the English SOP, Chinese SOP, matrices, quick cards, or manager add-ons.

## 5. Accessibility and safety gates

| Gate | Result |
| --- | --- |
| Required information remains available without images | Pass |
| Every local image use has meaningful, action-based alt text | Pass |
| No dialogue or instruction is baked into raster art | Pass |
| White panels preserve black lines in light and dark GitHub themes | Pass |
| Cobalt is decorative and never the sole carrier of meaning | Pass |
| Scenes avoid identity labels, sexualization, caricature, and authority worship | Pass |
| Coffee scene keeps a visible, unobstructed exit | Pass |
| Lunch scene depicts leaving without social penalty | Pass |
| Manager scene does not portray appeasement or domination | Pass |
| Collapsed summaries still identify each exercise | Pass |
| Interaction works without JavaScript or pointer-only gestures | Pass |
| Badge images have alt text and carry no essential information | Pass |
| External badge failure does not block navigation or content | Pass |
| Each local raster stays below the 1.2 MB project limit | Pass |

Result: **14/14 passed**. A future failure blocks visual release regardless of score.

## 6. GitHub rendering and technical review

The README was submitted to GitHub's Markdown rendering API in repository context. The output preserved:

- the responsive hero image with alt text;
- all four `<details>` and `<summary>` pairs;
- centered title, subtitle, badges, and navigation links;
- tables, callouts, headings, block quotes, and bilingual text.

The external language badge returned HTTP 200 during review. Badges remain nonessential and use descriptive alt text.

The checker validates required illustrations, PNG signatures, the 1.2 MB size ceiling, release markers, internal links, Markdown and HTML image paths, alt text, placeholders, scenario numbering, and refined line length.

## 7. Score

| Criterion | Weight | Score | Reason |
| --- | ---: | ---: | --- |
| Visual coherence | 20 | 19 | One restrained system across three distinct scenes |
| Navigation and scanability | 15 | 15 | Clear routes, numbered sections, compact repository map |
| Useful interaction | 15 | 14 | Four no-script exercises; GitHub cannot persist progress |
| Accessibility | 20 | 20 | Alt text, text parity, contrast, no color-only meaning |
| Cultural, power, and safety fit | 15 | 15 | Optionality and equal dignity are visible in scene composition |
| Performance | 10 | 9 | Local assets meet the limit; badges still require an external request |
| Maintainability | 5 | 5 | Asset notes, prompts, rules, and automated gates are documented |
| **Total** | **100** | **97** | Pass |

## 8. Limitations

- The illustrations were produced with an image-generation tool, then selected, inspected, and resized. They are not commissioned hand drawings.
- Editorial criteria reduce familiar generated-image clichés but cannot prove that every viewer will perceive the work as handmade.
- A white comic panel is visible against GitHub dark mode. This is intentional so black line work does not disappear.
- GitHub controls Markdown styling, spacing, heading anchors, and `<details>` behavior; these may change.
- Shields.io badges depend on an external service, but their information is repeated in text.
- No screen-reader, low-vision, cognitive-accessibility, or cross-device user study was conducted for v1.3.

Field feedback should focus on image interpretation, alt-text usefulness, mobile scanning, dark-theme comfort, cultural stereotyping, page weight, and whether the exercises reduce or add anxiety.

## 9. Final decision

**Pass v1.3.0 for inclusion, subject to local checks and GitHub Actions on the published commit.**

The visual system is approved because it adds recognition and practice without becoming image-dependent, decorative clutter, compulsory interaction, or a separate product surface.

If future work adds image-only instructions, missing alt text, stereotype-based characters, unreadable dark-mode art, remote scripts, or an asset above the size limit, stop release and rerun all 14 gates after correction.

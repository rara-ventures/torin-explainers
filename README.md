# torin-explainers

A research vault for short-form history and geopolitics videos, written in the style of Torin Russell's explainers. It is plain Markdown and opens as an **Obsidian vault**. There is no build step, no app and no test suite. The "product" is researched notes and **script-ready story cards** for TikTok/YouTube videos.

> **Agents: read this file first, then the README of the lab you are working in.** Every lab has its own `README.md` and, where one exists, a `thesis.md` that sets the rules for what counts as a claim.

---

## 1. What is in here

The vault is a series of "labs." Each lab is a research collection that builds on the one before it:

| Phase | Folder | What it is | Start at |
|---|---|---|---|
| 0 | `original/` | **Archive.** 100 Torin Russell explainers (website, 2026-05-07 → 2026-10-26) plus their 100 matching TikTok scripts, 6 cross-explainer "crazy stories", a knowledge graph and fact verification. | `original/README.md` |
| 0 | `tiktok/`, `youtube/` | **Channel data.** All 299 scraped TikTok videos (one stub each, with views and duration) and 7 YouTube long-form videos. `tiktok/scrape.py` is the only code in the repo. | `tiktok/README.md` |
| 1 | `tiktok-stories/` | **Scripts.** 14 Torin-style scripts on Indianization topics, each with 3+ cold-audience hooks, plus the hook playbook and research trails. | `tiktok-stories/README.md`, `HOOKS.md` |
| 2 | `indianization/` | **"The Sanskrit Cosmopolis"**: how Indian script, kingship, law and religion spread across SE Asia (500 BCE–1500 CE) without conquest. 19 century folders, 19 regions, 6 vectors, traces, about 600 dated timeline rows. | `indianization/Dashboard.md`, `thesis.md` |
| 3 | `food-passports/` | **"Every national dish is an immigrant"**: Columbian Exchange-centred food history. 18 crop passports, 10 dishes, 9 kitchens, 6 vectors, 6 waves, 5 traces, and a **story layer** of 34 ranked reveal cards. | `food-passports/Dashboard.md`, `stories/Story Bank.md` |

Shared vault infrastructure:

- `Categories/`: one hub note per category (`[[Champa]]`, `[[Food Passports]]`, `[[TikTok Stories]]` …). Notes link *to* these and do not live in them.
- `Templates/`: note templates (Inscription, Temple, Century, Food Passport, Dish, Kitchen).
- `Templates/Bases/*.base`: Obsidian **Bases** (native database views). These are the dashboards, and they filter on frontmatter.
- `.obsidian/types.json`: declares frontmatter property types (`century_num: number`, `region: multitext`, `mainstay: checkbox` …). **If you add a new property, add it here too.**

## 2. Layout

```
torin-explainers/            ← open this folder as the Obsidian vault
├── README.md                ← you are here (agent onboarding)
├── .obsidian/               ← types.json, templates.json (workspace*.json is gitignored)
├── Categories/              ← 48 category hub notes
├── Templates/               ← note templates + Bases/ (20 .base files)
├── original/
│   ├── sources/             ← 100 website scripts, VERBATIM — do not edit
│   ├── script/              ← 100 TikTok captions for comparison (see COMPARISON.md)
│   ├── stories/ categories/ connections/ verification/
├── tiktok/                  ← all-videos/ (299 stubs) + scrape.py
├── youtube/long-form/       ← 7 long-form video notes
├── tiktok-stories/          ← NN-slug.md scripts + HOOKS.md, RATINGS.md, *-CONNECTIONS.md, TWO-HOP-STORIES.md
├── indianization/
│   ├── Dashboard.md thesis.md
│   ├── sources/NN-Nth-century/   ← "<Nth> Century CE.md" + "<Nth> Century CE — Timeline.md"
│   ├── regions/<slug>/           ← "<Region> — Region.md" + "<Region> — Timeline.md"
│   ├── vectors/<slug>/           ← "<Vector> — Vector.md" + "<Vector> — Timeline.md"
│   ├── traces/ visualizations/ resources/
└── food-passports/
    ├── Dashboard.md thesis.md
    ├── passports/ dishes/ regions/ vectors/ sources/(waves w0–w5) traces/
    ├── stories/                  ← NN-slug.md cards + Story Bank.md + Connections Web.md
    └── visualizations/ resources/
```

## 3. Conventions (follow these and the Bases keep working)

### Frontmatter is the data model
Every note carries YAML frontmatter, and the Bases filter on it. Kepano-style:

```yaml
categories: ["[[Indianization Sources]]", "[[Champa]]"]   # always a LIST of wikilinks
region: ["Champa"]          # multitext lists
vector: ["Buddhism"]
century: "8th"              # text label
century_num: 700            # number, used for sorting
indianized: true            # thesis test (indianization)
unit: ["story"]             # food-passports: drives every food Base
created: 2026-11-09
status: draft
```

- Bases filter with `list(categories).contains(link("X"))`. Keep `categories` a list even when it has a single value.
- `indianization/` notes use `century`/`century_num`/`phase`/`region`/`vector`.
- `food-passports/` notes use `unit:` (`passport`, `dish`, `kitchen`, `vector`, `wave`, `trace`, `story`, plus `timeline` on ledger notes), `crop`, `kitchens`, `vectors`, `wave`/`wave_num`, `mainstay`.
- Start new notes from the matching file in `Templates/`.

### Status ladder
`todo` → `stub` → `draft` → `complete` → `verified` (and `deprecated` for superseded notes).
Script-facing notes use `needs-verify` → `ready` / `script-ready`.
- `complete` means written and reviewed, with secondary sources cited and debates flagged.
- `verified` means the primary anchor has been checked (inscription, annal, cookbook edition, ship record).
- Never promote a note without doing the check. The current backlog is mostly `stub` and `draft` (about 130 notes).

### Thesis tests (the bright lines)
- **Indianization** (`indianization/thesis.md`): a polity counts as Indianized only if it adopts **≥2 of** Indic script / dharmashastra law / Indic kingship / Buddhist-Shaiva state cult. Trade alone does not count. Regions are split into **core, conservatory, relay and outer**.
- **Food passports** (`food-passports/thesis.md`): the "naturalized citizen" test (`mainstay:`) separates a crop that settled from one that only passed through.

### Story card formats
- **Food story cards** (`food-passports/stories/NN-slug.md`): **assumption → reveal → proof stamps → kicker** (sometimes a "twist on the twist"). They carry a `tier: S|A|B` and are ranked in `Story Bank.md`. Chains of cards are listed in `Connections Web.md`. Mark any shaky fact inline with `⚠verify`.
- **TikTok scripts** (`tiktok-stories/NN-slug.md`): frontmatter has `hook`, `duration`, `region`, `century`. Each script has 3 hooks from *different* categories, a hook-variation table with 3–7 word text overlays, and then the script.
- **Cold-hook rule** (`HOOKS.md`): the first 3 seconds assume zero knowledge. Use only well-known anchors (Vietnam, Indonesia, India, Italy …) and never jargon like "Champa" or "Srivijaya" in the hook. Hook categories are numbered 01–10 (Curiosity, Contrarian, Authority, Emotional, Listicle, Question, Story, Negation, Specificity, Confession).
- Channel data says the best format is a **3–5 minute paradox explainer**, not an 80-second reel (`tiktok-stories/VIRAL-CONNECTIONS.md`).

### Links and files
- Use Obsidian wikilinks (`[[01-tomato-italy]]`, `[[Champa]]`) inside notes and relative Markdown links inside READMEs.
- File names contain **spaces and em dashes** (`Champa — Region.md`). Always quote paths in shell commands. In zsh, pass `--include='*.md'` quoted, and don't start an `echo` argument with `=`.
- When you rename a file, use `git mv` and update every link to it (`grep -rn` for the old name).
- Numbered cards and scripts are zero-padded (`NN-slug.md`). Pick the next free number.

### Research hygiene
- Every dated claim needs a source and a confidence note. Flag low-confidence claims and name the scholarly disagreement instead of smoothing it over.
- Each lab's `resources/Deep Research Prompt.md` is the standard procedure for moving a note one grade up the status ladder. Run it on one note at a time.
- `original/sources/` is the untouched archive and must stay citable. Never edit it.

## 4. Common tasks

| Task | Do this |
|---|---|
| Add a food story | Copy an existing card's shape → `food-passports/stories/NN-slug.md` (`unit: ["story"]`, `tier`, `status`) → add a row to `Story Bank.md` → add it to a chain in `Connections Web.md` if it links to other cards. |
| Add a TikTok script | `tiktok-stories/NN-slug.md` with `categories: ["[[TikTok Stories]]"]` → add it to the Files table in `tiktok-stories/README.md`. |
| Add an inscription or temple | Use `Templates/Inscription Template.md` / `Temple Template.md` → set `century`, `century_num`, `region`, `vector` → add a row to the relevant `— Timeline.md`. |
| Add a region, vector or crop | Create the folder or note pair, a `Categories/<Name>.md` hub, and check that the relevant `.base` picks it up. Update the counts in the lab README. |
| Fill a stub | Follow that lab's `resources/Deep Research Prompt.md`, then bump `status`. |
| Re-scrape TikTok | `python3 tiktok/scrape.py` (needs `yt-dlp`). Expect about 299+ videos. |

After any structural change, **update the counts and trees in the lab README** and in this file. Stale counts have needed fixing before (see git log).

## 5. Git

- Remote: `github.com/rara-ventures/torin-explainers`, branch `main`.
- Commit style is `scope: summary`. Scopes used so far: `content:`, `fix:`, `feat:`, `docs:`, `refactor:`, `research:`, and lab paths such as `food-passports/stories:`. Bodies are dense and list exactly what was added.
- Commit only when the user asks.

## 6. Using it in Obsidian (humans)

1. Open the folder as a vault. Bases is a core plugin.
2. Open `indianization/Dashboard.md` or `food-passports/Dashboard.md` to see live tables.
3. Useful Bases: `Champa.base`, `Buddhism.base`, `Thesis.base` (core vs relay), `Centuries.base`, `Passports.base`, `Dishes.base`, `TikTok.base`.

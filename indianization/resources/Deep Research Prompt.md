---
categories: ["[[Indianization Sources]]"]
kind: prompt
status: complete
created: 2026-11-08
---

# Deep Research Prompt

A reusable prompt for pushing a note from *written* to *evidenced*. It uses the sources layer in [[Watch & Listen]] as the entry point, but treats media as orientation and epigraphy as proof.

**How to use:** copy everything between the two rules into an agent that has read access to this repo. Fill the `{}` variables. Run it one note at a time, or use §7 for a batch sweep.

---

## PROMPT

**Role.** You are a research historian of South and Southeast Asia working inside the `torin-explainers` Obsidian vault. You know Old Khmer, Old Cham, Old Malay and Sanskrit epigraphy well enough to tell a *terminus post quem* from a *terminus ante quem*, and you are allergic to confident prose built on one secondary source.

**Target.** Note: `{PATH_TO_NOTE}` · Timeline: `{PATH_TO_TIMELINE}` · Vector/category: `{CATEGORY}` · Budget: `{900–1200}` words added or changed.

**Objective.** Raise this note's evidentiary confidence by one grade — `draft → complete → verified` — using primary sources wherever they exist, and by explicitly bounding the claims where they do not. You are not rewriting the note; you are auditing it and repairing what fails.

### 1. Build the claim register before you read anything else

Extract every checkable assertion in the note into a working table. One row per claim, not per sentence:

| # | Claim (as written) | Type | Anchor | Status | Verdict |
|---|---|---|---|---|---|
| 1 | C.40 is the oldest Sanskrit inscription in SE Asia | epigraphic | C.40 / Zakharov 2010 | contested | confine |
| 2 | Liu Fang took 1,350 Buddhist works in 605 | textual | *Sui shu* 64 | single-source | confirm |

`Type` ∈ date · name · number · place · causal · attribution. `Status` ∈ primary-attested · single-source · inference · unsourced · contradicted.

### 2. Rank the evidence, in this order

| Tier | What counts | Examples |
|---|---|---|
| 1 | Primary text, edition, translation, or object record | C.40, C.96, K.235, Kedukan Bukit, *Liang shu* 54, *Sui shu* 64, Yijing, Ibn Rustah, *Nagarakretagama* |
| 2 | Peer-reviewed scholarship with its own citations | Coedès 1968; Vickery 2005; Schweyer 2012; Pollock 2006; Griffiths 2014; Miksic 2013 |
| 3 | Reference works and syntheses | EI, Britannica, museum catalogues, *Ancient Southeast Asia* |
| 4 | Media, lectures, podcasts, documentaries | Fall of Civilizations, In Our Time, Great Courses |

Tier 4 tells you **where to look and what the consensus sounds like**. It never appears in a `## Sources` line for a factual claim and never overrides Tier 1. If a podcast and an inscription disagree, the inscription wins and the disagreement goes in `## Debates & confidence`.

### 3. Hunt the anchor

For each Tier-1 row, go to the corpus, not the summary:

- **Cham:** C.40, C.96, C.174, C.38, C.66 via EFEO / SEAlang Classics; note the edition and, where possible, the line.
- **Khmer:** K.235, K.604, K.842 via EFEO; check *saka* year → CE conversion yourself (add 78, subtract 1 for the elapsed year).
- **Malay:** Kedukan Bukit, Talang Tuwo, Kota Kapur via de Casparis 1956 or later editions.
- **Chinese:** *Liang shu*, *Sui shu*, *Xin Tang shu*, *Song shi* — cite chapter, not "Chinese annals". Prefer an accessible translation (Wheatley, Pelliot, Hirth & Rockhill) and say which.
- **Sanskrit/Pali:** GRETIL for the text; PTS / SuttaCentral for Pali; check the *Mahāvaṃsa* and *Cūḷavaṃsa* chapters directly.
- **Secondary:** resolve the DOI or publisher page (Crossref, OpenAlex, JSTOR, Project MUSE, Persée, HAL). Find the page number that supports the sentence. If you cannot, the citation is decorative — flag it.

### 4. Adjudicate each claim into one of five verdicts

| Verdict | Action |
|---|---|
| **confirm** | leave prose; upgrade the citation to include edition + page/line |
| **revise** | change the fact; keep the sentence rhythm |
| **confine** | keep the claim but attach its limit: "on the 605 figure, which rests on a single annal" |
| **split** | contested date → give both readings with the scholar attached |
| **delete** | no Tier 1–2 support and it is load-bearing → remove, and say so in the report |

Hard rules: never invent an inscription, a chapter number, a page, a URL, or a quotation. Never silently change a date — every changed date carries a one-line reason. "No evidence found" is a finding, not a failure; "evidence of absence" requires a search you can describe. If a link 404s, write that down rather than substituting a plausible one.

### 5. Write back, minimally

- Preserve frontmatter keys and vocabulary (`categories`, `region`, `vector`, `century`, `century_num`, `phase`, `status`, `indianized`).
- Add or replace rows in `## Key sources` — `| Type | Source | Date |`, primary before secondary.
- Rewrite `## Debates & confidence` so each contested point names the scholars on both sides and says what would settle it. This section is the deliverable, not a disclaimer.
- Append unresolved rows to the timeline with `Confidence: low` and the reason in the Source cell; never delete an existing row because it is inconvenient.
- Keep `## Watch & listen` as-is unless a link is dead.
- 900–1,200 words of net change. No new sections unless §6 says otherwise.

### 6. Only add a section if the evidence earns one

Add `## What the inscription actually says` when a Tier-1 text exists and the note currently paraphrases it. Quote ≤ 3 lines, give the edition, then translate plainly. This is the highest-value addition in the whole vault and should be used sparingly.

### 7. Batch mode (optional)

For a low-confidence sweep, process notes in order of weakest evidence. Output one claim register per note, but only commit edits where the verdict is **revise**, **split** or **delete**; queue **confine** edits into a single pass at the end so the prose stays consistent.

### 8. Report back in this exact shape

1. **Verdicts** — counts of confirm / revise / confine / split / delete.
2. **Changes** — file, line, before → after, one line each.
3. **New anchors** — inscription or chapter now cited, with edition.
4. **Dead ends** — what you could not verify, and what you tried.
5. **Grade** — `draft` / `complete` / `verified`, with the reason in one sentence.
6. **Next target** — the claim in this note most likely to be wrong.

---

## Confidence rubric

| Grade | Test |
|---|---|
| **verified** | every load-bearing claim has a Tier-1 anchor or two independent Tier-2 sources, and contested points are stated as contested |
| **complete** | all load-bearing claims have Tier-2 support; Tier-1 anchors exist for the key dates but have not been read at source |
| **draft** | structure and narrative are sound; at least one load-bearing claim rests on a single source or an inference |
| **deprecated** | superseded by a later note or by scholarship that contradicts its spine |

## Short form (one paragraph, for a single claim)

> Verify this claim against a primary source: "{CLAIM}" in `{NOTE}`. Find the inscription, chapter or edition that would settle it, quote the relevant line, and tell me whether the note should keep, soften, split or drop the claim. If the only support is a podcast or a synthesis, say so and mark it low confidence. Do not invent a citation.

## What this prompt is designed to catch

- A date that drifted between two editions of Coedès and is now cited to neither.
- A "first" claim (oldest inscription, first kingdom) that a newer article has already narrowed.
- A number from a Chinese annal repeated without its single-source caveat.
- A causal sentence ("X caused the shift to Y") standing on correlation in one secondary source.
- A media link presented as evidence.

---

*Related: [[Watch & Listen]] · [[indianization/thesis|Thesis]] · [[indianization/Dashboard|Dashboard]]*
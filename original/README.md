# Torin Russell — Explainers Archive

> Every script from former intelligence analyst Torin Russell's geopolitics videos, now a research lab.
> Source: https://torinrussell.com/explainers — Downloaded 100 explainers (2026-05-07 to 2026-10-26) as Markdown via Squarespace JSON API.

## Structure

```
torin-explainers/
├── sources/          — 100 original scripts as .md (YAML frontmatter + Markdown body)
├── stories/          — 6 curated crazy stories that connect the dots
├── categories/       — 7 thematic clusters (beyond site categories)
├── connections/      — knowledge graph (Mermaid) linking all 100
├── verification/     — internet-checked facts + added details
└── README.md         — you are here
```

## Originals → Sources

All 100 originals are preserved verbatim in `sources/` (git `R` history from root). Each has:
- YAML: `title`, `date`, `url`, `categories`, `tags`, `slug`, `author`
- Body: HTML → Markdown via BeautifulSoup (links absolutized, `*em*`, `**strong**`, `###` / lists)

See `sources/how-did-japan-end-up-controlling-chinas-gateway-to-the-pacific.md` for example. Site pagination: 5×20 (`?format=json&offset=...`), verified no HTML leaks, byte-identical to remote.

## The Six Crazy Stories (Start Here)

| # | Story | Explainers | Hook |
|---|-------|------------|------|
| 1 | [The Immortals](./stories/01-the-immortals.md) | 12 | Why San Marino (1.6 cars/person) & Guam (DF-26 target) both cheat death — 4 cheat codes of microstates |
| 2 | [The Nuclear Heartbeat](./stories/02-the-nuclear-heartbeat.md) | 8 | Warheads rot (12.32y tritium), satellites loop (63.4° Molniya), presidents get 6 minutes |
| 3 | [The Map That Eats Its People](./stories/03-the-map-that-eats-its-people.md) | 11 | How Berlin's pencil (Gambia 10km) → cobalt → coups — Africa's engineered chaos |
| 4 | [The Language Ghosts](./stories/04-the-language-ghosts.md) | 8 | Hungarian 3,000km from Siberia, Wales vs Ireland, Basque fiscal sovereignty |
| 5 | [The Straitjacket Archipelago](./stories/05-the-straitjacket-archipelago.md) | 14 | Ryukyu 1,200km wall, Kaliningrad, India-Bangladesh counter-counter-enclave, Ceuta |
| 6 | [The Shadow Sovereigns](./stories/06-the-shadow-sovereigns.md) | 9 | Popes, nobles, Lloyd's 72h, Liberia's Virginia flag factory, contractors |

Each story weaves 8-14 explainers into a narrative arc, cites `sources/...md:line` and adds external verification.

## Categories (Original vs Curated)

**Original site categories:** Europe 25, Africa 19, Asia 18, Russia & Eurasia 12, North America 10, Latin America 9, Middle East 6, Oceania & Pacific 5, Caribbean 4, Global 3

**Curated thematic clusters** in `categories/`:

- [The Immortals](./categories/the-immortals.md) — 12 microstates/buffers
- [Nuclear Shadow](./categories/nuclear-shadow.md) — 8
- [Engineered Borders & Enclaves](./categories/engineered-borders-and-enclaves.md) — 9
- [Straitjacket Archipelago](./categories/straitjacket-archipelago.md) — 9
- [Africa Engineered Chaos](./categories/africa-engineered-chaos.md) — 11
- [Language Ghosts](./categories/language-ghosts.md) — 8
- [Shadow Sovereigns](./categories/shadow-sovereigns.md) — 9

Full index: [`categories/README.md`](./categories/README.md). Tags: Democracy & Governance 24, Economy & Trade 22, Conflict 20, Colonial Legacy 17, Military & Defense 16…

## Connections Graph

[`connections/GRAPH.md`](./connections/GRAPH.md) — Mermaid graph with 100 nodes, 6 clusters, and 5 surprise bridges:
- San Marino cars ↔ Liberia flags (registration arbitrage)
- Bhutan villages ↔ tritium decay (satellite-measured)
- Molniya 63.4° ↔ Danish Straits 1857 (latitude math)
- Eritrea 10% Bab el-Mandeb ↔ Lloyd's 10% Hormuz
- Paraguay Itaipú ↔ Bhutan hydro (identical must-sell clause)

## Verification

[`verification/VERIFICATION.md`](./verification/VERIFICATION.md) — 8 internet-checked claims with sources:

- San Marino 1,606/1k vehicles (WHO 2018, WorldPopulationReview 2024) ✅
- Molniya 63.4° frozen orbit ( `4-5 sin²i=0` ) ✅
- Tritium 12.323 y (DOE-STD-1129-2015, EPA, NRC) ✅
- Andorra + San Marino **signed 19 Oct 2026** (EU IP_26_2182, Diari d'Andorra) ✅ — joint signing updates Torin's earlier "scheduled" language
- Bhutan 22 villages, 2,200 homes, 2% annexed (NYT 2024, Reuters 2022, CNN 2024, Diplomat 2024) ✅
- India-Bangladesh counter-counter-enclave Dahala Khagrabari ✅
- etc. — methodology and remaining flags documented.

## GitHub

Public mirror: **https://github.com/rara-ventures/torin-explainers** — `main` branch, initial 100 + reorg.

## How to Use

- **Research:** Start with a story (e.g., `stories/01-the-immortals.md`), follow `sources/` links, check `verification/` for external receipts.
- **Browse by theme:** `categories/the-immortals.md` gives a table with dates/tags.
- **Visual:** `connections/GRAPH.md` renders in GitHub.

---

*Built 29 Oct 2026 — all scripts © Torin Russell, archived for research.*

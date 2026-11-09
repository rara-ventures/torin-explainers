# torin-explainers — Geopolitics → Indianization, Obsidian Vault

> Two labs, one vault. Built for Obsidian Bases (Kepano style) — filter, sort, visualize without plugins.

## Vault Layout

```
torin-explainers/  ← Open this folder as Obsidian Vault
├── .obsidian/          ← types.json (+century/region/vector), templates.json
├── Categories/         ← [[Indianization Sources]], [[Champa]], [[YouTube Long Form]], etc.
├── Templates/
│   ├── Inscription Template.md
│   ├── Temple Template.md
│   └── Bases/          ← 13 Bases: Sources, Champa, Buddhism, Centuries, Indianization, Thesis, YouTube, TikTok...
├── original/           ← 100 Torin Russell explainers + 100 TikTok scripts + 6 stories
├── indianization/      ← South Asian history: Champa → Buddhism in Indonesia
│   ├── Dashboard.md    ← START HERE (embeds all Bases)
│   ├── sources/        ← 19 century folders (BCE–16th), each with century note + timeline
│   ├── regions/        ← 19 regions (Champa, Srivijaya, Sailendra, Philippines...)
│   ├── vectors/        ← 6 mechanisms (Buddhism, Pallava Script...)
│   ├── traces/         ← Narratives (champa-to-borobudur-buddhism.md)
│   ├── visualizations/ ← Mermaid maps & matrix
│   └── resources/      ← Watch & Listen media index
├── tiktok/             ← 299 scraped channel videos + scraper
├── tiktok-stories/     ← 7 cold hooks (70 variations, rated)
└── youtube/            ← YouTube long-form (7 videos, 6–24 min)
```

## Open in Obsidian

1. **Open Folder** → select `torin-explainers`
2. Install **Bases** core plugin (enabled by default 2024+)
3. Open `indianization/Dashboard.md` — you see live tables; add `century: "8th"` to any note and it resorts.
4. Use **Command Palette → Bases: Open** to filter.

## Filter Cheat Sheet (Your Question)

| Want | Open | Filter |
|------|------|--------|
| Champa only | `Templates/Bases/Champa.base` | `list(categories).contains(link("Champa"))` OR `region.containsAny("Champa")` |
| Buddhism in Indonesia | `Templates/Bases/Buddhism.base` | `region.containsAny("Sailendra Mataram","Srivijaya","Kedah Srivijaya") && vector.containsAny("Buddhism")` |
| Champa → Borobudur path | `Templates/Bases/Indianization.base#Champa → Java Trace` | Pre-filtered (3 regions + 2 vectors) |
| Core vs relay | `Templates/Bases/Thesis.base` | `indianized == true` (core) / `false` (relay) |
| By century | `Templates/Bases/Centuries.base` | `sort: century_num ASC` |
| Everything | `Templates/Bases/Indianization.base` | All Indianization sources |

## Create a New Note

- **Inscription:** `Templates → Inscription Template` → set `century:`, `region:`, `vector:` → appears in Bases instantly.
- **Temple:** `Templates → Temple Template` → same.

## Why This Organization?

- **Kepano pattern:** `categories: ["[[X]]"]` list per note, `topics: []` multitext, `created:` date — Bases filter via `list(categories).contains(link("X"))` (list-wrapped so single- and multi-value notes behave the same).
- **Combined 2+3:** Phased centuries (historically coherent) + matrix (century×region×vector) via `Dashboard.md` embeds. You get strict centuries *and* thematic views.
- **Champa → Indonesia trace** is first-class: `indianization/traces/champa-to-borobudur-buddhism.md` stitches 5th–9th c. via Srivijaya bridge.

## GitHub

https://github.com/rara-ventures/torin-explainers — `main`

---
*Built 29 Oct 2026 · audited 1 Nov 2026 — Obsidian Bases + Kepano vault compatible.*

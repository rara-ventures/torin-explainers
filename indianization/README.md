# The Sanskrit Cosmopolis — How India Traveled Without Conquering (500 BCE–1500 CE)

> From Kaundinya's Naga bride in Funan to Borobudur's 2,672 reliefs and Bali's living Hinduism — how India traveled without conquering.

**This lab is Phase 2 of `torin-explainers`.** `original/` holds 100 Torin Russell scripts (geopolitics explainers). `indianization/` is a new research collection tracing one long arc you asked for: **Champa (Vietnam) → Buddhism in Indonesia**.

## Structure (Hybrid: Phased Centuries + Matrix)

```
indianization/
├── sources/          century folders (BCE–16th) — each: README.md (story list) + timeline.md
├── regions/          18 polities (Gandhara, Himalaya, Lanka, China, Persia, Rome + 10 SE Asia + Straits/Mainland)/sites — each: README.md + timeline.md
├── vectors/          6 mechanisms — each: README.md + timeline.md
├── traces/           cross-cutting narratives (Champa → Borobudur)
├── visualizations/   master timelines & maps (Mermaid)
└── README.md         you are here
```

You asked for `indianization/sources/` with century folders, story lists, and timeline + visualization. Built as requested **plus** `regions/` and `vectors/` so you can follow a *place* (Champa) or a *vector* (Buddhism) across centuries — not just a date.

## The 6 Phases (Your Centuries Grouped)

| Phase | Centuries | Shorthand | What Happened |
|-------|-----------|-----------|---------------|
| **0 Prelude** | BCE–1st | Ashoka & Austronesian ships | Mauryan dhamma missions, Tamil Sangam trade, Dong Son contacts |
| **1 Contact** | 1st–4th | Funan & Vo Canh | Funan (Oc Eo) entrepôt, Vo Canh Sanskrit 2nd c., Champa Lâm Ấp |
| **2 Transplant** | 5th–7th | Gupta–Pallava → Chenla | Chenla replaces Funan, Dvaravati (Mon), Kedah, Pallava script, Gupta art |
| **3 Classical** | 8th–10th | Sailendra, Srivijaya, Angkor | Borobudur (~782–835), Prambanan, Srivijaya (Kedukan Bukit 683), Angkor 802 |
| **4 Imperial** | 11th–13th | Chola & Angkor | Angkor Wat 1113, Chola raid 1025 on Kedah/Srivijaya, Pagan, Theravada turn |
| **5 Transition** | 14th–16th | Majapahit → Islam | Majapahit, Sukhothai, Malacca 1402, Champa Vijaya 1471 falls, Bali refuge, Portuguese 1511 |

Each `sources/XX-century/` lives inside its phase — see `sources/README.md` for the gantt.

## Start Here: Champa → Buddhism in Indonesia

**Your path:** `traces/champa-to-borobudur-buddhism.md` — follows one vector (Mahayana/Vajrayana) across two regions (Champa's Po Nagar & My Son → Java's Borobudur), 5th–9th centuries, via Srivijaya as bridge and Pallava script as vehicle. Includes map + timeline + inscriptions (Po Nagar C.96, Kedukan Bukit 683, Kalasan 778).

Jump: **→ [`traces/champa-to-borobudur-buddhism.md`](./traces/champa-to-borobudur-buddhism.md)**

Or pick an axis:

- **By century:** [`sources/08-8th-century/README.md`](./sources/08-8th-century/README.md) (Borobudur), [`sources/04-4th-century/README.md`](./sources/04-4th-century/README.md) (Vo Canh)
- **By region:** [`regions/champa/README.md`](./regions/champa/README.md) (Vietnam), [`regions/sailendra-mataram/README.md`](./regions/sailendra-mataram/README.md) (Java), [`regions/kedah-srivijaya/README.md`](./regions/kedah-srivijaya/README.md) (bridge)
- **By vector:** [`vectors/buddhism/README.md`](./vectors/buddhism/README.md) (how Buddhism traveled), [`vectors/art-architecture/README.md`](./vectors/art-architecture/README.md)

## Visualizations

- **Master century gantt:** [`sources/README.md#gantt`](./sources/README.md)
- **Spread map (Mermaid):** [`visualizations/spread-map.md`](./visualizations/spread-map.md)
- **Influence matrix (region × vector):** [`visualizations/influence-matrix.md`](./visualizations/influence-matrix.md)
- **Full graph:** [`../original/connections/GRAPH.md`](../original/connections/GRAPH.md) (100 Torin explainers) + this lab's Mermaid in `sources/README.md`

## Status

- Scaffolding: ✅ 17 century folders, 10 regions, 6 vectors, 1 trace — all with `timeline.md` placeholders
- Sources ingestion: ⬜ TODO — next step is to fill `sources/*/timeline.md` with dated inscriptions (Vo Canh, My Son, Kedukan Bukit, Kalasan, Borobudur) + Chinese annals (Liangshu on Funan, Songshi on Champa)
- `original/` is untouched history (git `R` from root), so Torin archive stays citable.

---

*Next: Fill a century (e.g., 08-8th) with 3 stories and verify via epigraphy?*

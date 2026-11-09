# Food Passports — Every "national" dish is an immigrant that got there first

> **Phase 3 lab of `torin-explainers`.** Same principles as `indianization/`: axes + Bases + traces.
>
> **Thesis:** the passport says one country, the flag says another. Tomatoes are Aztec immigrants in Italy, potatoes arrived in Nepal's mid-hills via Portuguese Goa and British India, chilies replaced timur and ji-tima in the Himalaya. Scope: **Columbian Exchange-centric but global** — the 1492+ waves, with the Old World pantry (Silk Roads, monsoon trade) as prelude so we can make connections.

## Structure

```
food-passports/
├── Dashboard.md         ← START HERE (embeds all Bases)
├── thesis.md            ← the "naturalized citizen" test (mainstay vs transit)
├── passports/           ← WHO travels — one note per crop (18: 14 outbound, 4 inbound)
├── dishes/              ← the proof — national dishes whose ingredients are immigrants (10)
├── regions/             ← WHERE they settled — adoption kitchens (9)
├── vectors/             ← HOW they traveled — routes & carriers (6)
├── sources/             ← WHEN — 6 wave folders (W0 prelude → W5 industrial)
├── traces/              ← stitched narratives (tomato→Naples, potato→Nepal, chili→Asia...)
├── visualizations/      ← Mermaid spread map + crop × kitchen passport matrix
└── resources/           ← Watch & Listen + Deep Research Prompt
```

## Mapping to indianization principles

| indianization | food-passports | Meaning |
|---|---|---|
| `regions/` | `regions/` (kitchens) | where the thing landed |
| `vectors/` | `vectors/` | how it traveled (ships, Goa hub, plantations, diaspora, industry) |
| `sources/` centuries | `sources/` **waves** | when — W0–W5 instead of 19 centuries |
| `traces/` | `traces/` | cross-axis narratives |
| `thesis.md` (`indianized:`) | `thesis.md` (`mainstay:`) | the bright-line test: citizen or transit? |
| inscriptions (proof) | dishes + festivals (proof) | pizza 1889, doubanjiang, Hemja Potato Festival 2025 |
| `Categories` + `.base` | same | `[[Food Passports]]` root; unit-filtered Bases |

## The 6 Waves

| Wave | Period | Shorthand | What Happened |
|---|---|---|---|
| **W0 Prelude** | before 1492 | The Old Pantry | wheat & noodles on Silk Roads, sugarcane New Guinea→India, spice monsoons; all heat was pepper — timur, ji-tima, pippali, Sichuan pepper |
| **W1 Ships & Seeds** | 1493–1550 | First stamps | Columbus's 1493 voyage carries seeds; 1498 Vasco da Gama → chilies reach Goa c. 1500; tomato described in Europe 1544 as ornamental |
| **W2 Galleons & Missions** | 1550–1650 | Two oceans | Manila Galleon from 1571: Mexican chilies/maize → Philippines, China, Japan; Portuguese spread cassava to Angola, papaya/cashew to Goa; sweet potato into Fujian 1590s |
| **W3 Peasants' Gardens** | 1650–1800 | Poor people adopt first | potato pushed by state (Prussia 1756, Parmentier 1770s); maize into West Africa & Qing highlands; Latini's 1692 Naples recipe — first "tomato sauce", labelled *alla spagnuola* |
| **W4 Naturalization** | 1800–1900 | Citizenship granted | pizza with tomato (1830s pizzerias; 1889 Margherita legend); paprika becomes Hungarian; Irish potato catastrophe 1845–52; chili reaches Nepal's mid-hills; red kimchi & Sichuan mala standardize; Japanese curry 1870s |
| **W5 Industrial Plate** | 1900–now | The brand erases the route | canning, frozen pizza 1957, Green Revolution (CIMMYT hybrids → Nepal 1960s–70s), instant noodles 1971; Nepal holds the **National Potato Festival at Hemja, Kaski** — the immigrant gets a parade |

## Your Path: One Crop, Two Oceans, Seven Kitchens

Start with `traces/chili-two-doors.md` — how a Amazonian shrub entered Asia through **two doors** (Goa and Manila) and rewrote Sichuan, Korea, Thailand, Nepal, Hungary on the way. Or the home angle: `traces/potato-to-nepal.md`.

## Status

- Scaffold: ✅ tree, 18 passports, 10 dishes, 9 kitchens, 6 vectors, 6 waves, 5 traces — all `status: stub` until the Deep Research Prompt is run per note.
- Bases: `Templates/Bases/Passports.base`, `Dishes.base`, `Kitchens.base`, `Waves.base`, `FoodVectors.base`, `FoodTraces.base`, `FoodPassports.base`
- Frontmatter convention: see `Templates/Food Passport Template.md`. `unit:` (multitext) drives every Base filter.

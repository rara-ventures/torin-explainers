---
categories: ["[[Indianization Sources]]"]
created: 2026-10-30
status: verified
---

# Thesis — What Counts as Indianization

> **Bright-line rule (Pollock-based, per audit 2026-10-30):** A polity is **Indianized** iff it adopts **≥2 of**:
> 1. **Sanskrit-derived script** (Pallava → Cham, Kawi, Khmer, Old Mon, Thai)
> 2. **Dharmashastra / niti** (Manusmriti, Kautilya, Mulagandha-style law)
> 3. **Indic kingship** (chakravartin, devaraja, linga, varna/brahmin legitimation)
> 4. **Buddhist/Shaiva state cult** (stupa/vihara, candi, devaraja Shaiva, Mahayana/Vajrayana)
>
> Trade alone (pepper for gold) is **not** Indianization.

## Core vs Relay vs Outer

| Zone | Polities | Indianized? | Role |
|------|----------|-------------|------|
| **Core Indianization** | Champa, Funan-Chenla, Dvaravati, Sailendra-Mataram, Kedah-Srivijaya, Angkor, Pagan, Majapahit, Bali, Sukhothai-Ayutthaya | ✅ Yes (≥2) | Adopted script + kingship + cult |
| **Conservatory / Source** | Sri Lanka (Theravada factory), Himalaya (Licchavi Sanskrit + Newar Vajrayana) | ✅ Yes | Conserved + re-exported |
| **Relay / Filter** | **Gandhara**, **Persia (Sasanian + Sogdians)**, **Rome/Byzantium**, **China** (as recipient-translator) | ❌ No — Relay | Transmitted without adopting; filtered via Kharosthi, Pahlavi Kalila, Periplus, Xuanzang/Yijing |
| **Relay detail** | Sogdian letters 313CE (Samarkand→Luoyang pepper/musk), Borzuya Kalila 540-570 (Sanskrit→Pahlavi→Arabic), An Shigao/Lokaksema 148-189 (Gandhari→Chinese), Muziris Papyrus (India↔Rome via Tamil) | — | See `regions/gandhara/timeline.md`, `regions/persia/timeline.md`, `regions/rome-byzantium/timeline.md`, `regions/china/timeline.md` |

> **Vault structure after audit:** `regions/` is now **12 core + 6 relay/outer**. Bases: `Regions.base` shows all 18 but `Thesis` filters `indianized:true` for core. Matrix demoted relay trade `●●●→●●○` with `via India` note.

## How India Traveled Without Conquering

India exported **grammar** (script, law, kingship, cult) not armies. Relays carried **goods + translations** but didn't become Indianized — proof by negative: Rome bought pepper with gold (Periplus) but kept Latin law; Persia taxed it at Ctesiphon but kept Pahlavi; China translated sutras but kept Confucian bureaucracy.

## See also

- `visualizations/spread-map.md` — dashed = relay, solid = Indianization
- `visualizations/influence-matrix.md` — `○○○` for relay = not Indianized, `●●●` = deep adoption
- `README.md` — scaffolding status

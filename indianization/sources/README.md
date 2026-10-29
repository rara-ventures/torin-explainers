# Sources — By Century

> Every century from BCE prelude to 16th c. afterglow. Each folder = `README.md` (story list) + `timeline.md` (dated events).

## Visualization — 6 Phases as Gantt

```mermaid
gantt
    title Indianization of Southeast Asia — Century Overview
    dateFormat  YYYY
    axisFormat %Y
    %% BCE as 0500 for plotting (500 BCE)
    section Phase 0 Prelude
    BCE–1st (Ashoka, Dong Son)       :done, 0000, 0100
    section Phase 1 Contact (1st–4th)
    1st Funan/Oc Eo                  :active, 0100, 0200
    2nd Vo Canh                      : 0200, 0300
    3rd Funan peak                   : 0300, 0400
    4th Champa My Son E1 / Gupta     : 0400, 0500
    section Phase 2 Transplant (5th–7th)
    5th Chenla/Dvaravati             : 0500, 0600
    6th Chenla/Funan end             : 0600, 0700
    7th Srivijaya 683                : 0700, 0800
    section Phase 3 Classical (8th–10th)
    8th Borobudur start              : 0800, 0900
    9th Prambanan/Angkor Hariharalaya: 0900, 1000
    10th Angkor Yasodharapura        : 1000, 1100
    section Phase 4 Imperial (11th–13th)
    11th Angkor Wat / Chola 1025     : 1100, 1200
    12th Bayon / Pagan peak          : 1200, 1300
    13th Sukhothai/Singhasari        : 1300, 1400
    section Phase 5 Transition (14th–16th)
    14th Majapahit peak              : 1400, 1500
    15th Malacca 1402 / Vijaya 1471  : 1500, 1600
    16th Bali refuge / Portuguese    : 1600, 1700
```

## Century Folders

| Folder | Century | Phase | Anchor Event | Trace Link |
|--------|---------|-------|--------------|------------|
| [`00-bce-prelude/`](./00-bce-prelude/) | BCE–1st | 0 Prelude | Ashoka rock edicts, Tamil-Bengal ships | → trade-maritime |
| [`01-1st-century/`](./01-1st-century/) | 1st | 1 Contact | Funan Oc Eo entrepôt, Kaundinya legend | → funan-chenla |
| [`02-2nd-century/`](./02-2nd-century/) | 2nd | 1 Contact | **Vo Canh** inscription (oldest Sanskrit) | → sanskrit-pallava |
| [`03-3rd-century/`](./03-3rd-century/) | 3rd | 1 Contact | Funan Fan Shiman, Champa Lâm Ấp | → champa |
| [`04-4th-century/`](./04-4th-century/) | 4th | 1 Contact | Champa My Son E1 (Bhadravarman), Gupta start | → champa |
| [`05-5th-century/`](./05-5th-century/) | 5th | 2 Transplant | Chenla rise, Dvaravati Dharma wheels | → dvaravati |
| [`06-6th-century/`](./06-6th-century/) | 6th | 2 Transplant | Champa My Son A1, Kedah proto-city | → kedah-srivijaya |
| [`07-7th-century/`](./07-7th-century/) | 7th | 2 Transplant | **Kedukan Bukit 683** (Srivijaya), Xuanzang | → kedah-srivijaya |
| [`08-8th-century/`](./08-8th-century/) | 8th | 3 Classical | **Borobudur start ~782**, Kalasan 778, Jayavarman II 802 | → sailendra-mataram |
| [`09-9th-century/`](./09-9th-century/) | 9th | 3 Classical | Borobudur done, Prambanan, Angkor Hariharalaya | → angkor |
| [`10-10th-century/`](./10-10th-century/) | 10th | 3 Classical | Yasodharapura (Angkor), Chola maritime | → angkor |
| [`11-11th-century/`](./11-11th-century/) | 11th | 4 Imperial | Angkor Wat 1113, **Chola raid 1025** on Srivijaya | → vectors/trade-maritime |
| [`12-12th-century/`](./12-12th-century/) | 12th | 4 Imperial | Bayon, Pagan peak, Theravada turn | → vectors/buddhism |
| [`13-13th-century/`](./13-13th-century/) | 13th | 4 Imperial | Sukhothai, Singhasari, Mongol Java 1293 | → majapahit |
| [`14-14th-century/`](./14-14th-century/) | 14th | 5 Transition | Majapahit Nagarakretagama | → majapahit |
| [`15-15th-century/`](./15-15th-century/) | 15th | 5 Transition | Malacca 1402, **Vijaya 1471** fall of Champa, Angkor 1431 | → champa |
| [`16-16th-century/`](./16-16th-century/) | 16th | 5 Afterglow | Demak, Bali Hindu refuge, Portuguese 1511 | → bali |

## How to Use

- **Chronological:** Start in a century → read its `timeline.md` → jump to `../../regions/<name>` for that polity's full arc.
- **Regional:** Starting from Champa? Open `champa` region then follow its timeline *across* centuries back to `sources/`.
- **Vector:** Following Buddhism? Open `vectors/buddhism` — it links to the century where Borobudur vs My Son diverge.

Each `README.md` inside a century lists *stories* (narratives) for that slice; each `timeline.md` is the dated ledger (inscriptions, temples, Chinese annals). Both are stubs — next ingestion fills them with cited sources.

## Next Visualization

- Region spread map → [`../visualizations/spread-map.md`](../visualizations/spread-map.md)
- Influence matrix (region × vector heat) → [`../visualizations/influence-matrix.md`](../visualizations/influence-matrix.md)

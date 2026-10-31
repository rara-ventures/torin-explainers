---
categories: ["[[Indianization Sources]]"]
created: 2026-10-30
status: draft
---

# Spread Map — How Indianization Traveled (Extended: Rome to Timor)

> ⚠️ **Audit 2026-10-30:** Arrows fixed per DeepSeek/GLM #4/#7. Solid = attested direct (Periplus, inscriptions, pilgrim accounts). Dashed = relay/inferred via intermediaries. `via:` labels added. See per-hop sources in region timelines.

```mermaid
flowchart LR
    Rome["Rome/Alexandria<br/>Periplus 40CE<br/>Muziris Papyrus"]
    Persia["Persia Ctesiphon<br/>Sasanian 224-651<br/>Sogdians Samarkand"]
    Gandhara["Gandhara<br/>Taxila/Peshawar<br/>Kanishka 78CE<br/>Bamiyan 507/554*"]
    Himalaya["Himalaya<br/>Nepal Licchavi 464<br/>Bhutan Kyichu 649†"]
    Lanka["Sri Lanka<br/>Mahinda 246BCE<br/>Anuradhapura<br/>Tooth Relic 310CE"]
    India["India<br/>Pallava Kanchi<br/>Nalanda<br/>Amaravati"]
    OcEo["Oc Eo (Funan)<br/>1st-6th<br/>Antoninus Pius 138-161<br/>deposited 200-300CE"]
    Kedah["Kedah<br/>Sungai Batu<br/>iron 535BCE* charcoal<br/>brick 110CE"]
    Srivijaya["Srivijaya Palembang<br/>683 Kedukan Bukit"]
    Champa["Champa My Son/Po Nagar<br/>Bhadravarman 380"]
    Java["Java Borobudur 782<br/>Sailendra"]
    Angkor["Angkor 802 Devaraja<br/>Wat 1113"]
    China["China<br/>Chang'an/Nalanda<br/>Xuanzang 629<br/>Yijing 671"]
    Pagan["Pagan 1057<br/>Theravada via Lanka"]
    Malacca["Melaka 1402<br/>Timor Sandalwood 1225†"]
    Luy Lau["Luy Lâu (Giao Chỉ)<br/>Mâu Tử 2nd c.<br/>Vinitaruci 580"]
    Dai Viet["Đại Việt<br/>Thang Long 1010<br/>One-Pillar 1049"]
    Timor["Timor 1225 Zhufan Zhi<br/>Ti-wu? disputed<br/>sandalwood via Javanese"]
    Bali["Bali Hindu refuge<br/>subak"]

    Persia -.->|Aramaic → Kharosthi 518BCE<br/>via Achaemenid| Gandhara
    Gandhara -->|Kharosthi scrolls 147-189<br/>Lokaksema in Luoyang| China
    Gandhara -->|Greco-Buddhist art| Himalaya
    Himalaya -.->|Bhrikuti 632 → Tibet<br/>Songtsen Gampo| Himalaya
    Himalaya -.->|Arniko 1260 → Beijing<br/>600y later| China
    India -->|Pallava script| Champa
    India -->|Pallava script 2nd c. CE| Kedah
    India -.->|Monsoon winds<br/>via Tamil brokers| OcEo
    Rome -.->|Gold for pepper<br/>Periplus/Muziris<br/>via India| India
    India -.->|Relay via Funan<br/>2 bracteates, not route| OcEo
    OcEo --> Kedah
    Lanka -->|Mahinda 246BCE<br/>Faxian 410| Lanka
    Lanka -->|Parakramabahu 1153<br/>Lankavamsa| Pagan
    Pagan -->|Lankavamsa via Martaban 1331| Sukhothai
    Lanka -.->|Lankavamsa 13th c.<br/>Sumana 20 monks| Sukhothai
    China -.->|Vinitaruci 580 Chan via Jiankang| Luy Lau (Giao Chỉ/Dai Viet)
    Luy Lau -.->|Thiền + One-Pillar 1049| Dai Viet
    Srivijaya -->|Yijing 671 maritime| China
    Kedah --> Srivijaya
    Srivijaya --> Champa
    Srivijaya --> Java
    Java --> Angkor
    Timor -.->|Sandalwood 1225†<br/>via Javanese/Gujarati| Malacca
    Kedah -.->|Entrepôt relay| Malacca
    Srivijaya -.->|Entrepôt| Malacca
    Java -->|Lontar palm to Bali 1527| Bali

    style India fill:#f9f,stroke:#333,stroke-width:2px
    style Srivijaya fill:#ff9,stroke:#333,stroke-width:2px
    style Gandhara fill:#ccf,stroke:#333
    style Rome fill:#fcc,stroke:#333
    style Persia fill:#ffc,stroke:#333
    style Timor fill:#eee,stroke:#999,stroke-dasharray: 5 5
```

> **Legend:** Solid = attested. Dashed = relay/inferred. `*` charcoal vs structure caveat (`Kedah 535BCE charcoal, brick 110CE; Bamiyan 507/554 ±30y`). `†` legendary/tradition (`Kyichu 649 traditional, fabric 8th c.; Timor Ti-wu? disputed per Ptak 1987`).
> **Fixes 2026-10-30:** `Persia(Aramaic)→Gandhara` (not India→Gandhara), `Rome→India→Oc Eo` (no direct Rome→Oc Eo), `Himalaya→Tibet` then `Arniko→China` (not Bhrikuti→China), `Srivijaya→China` (not China→Srivijaya), `Timor→Malacca via Javanese` (not Kedah→Malacca). Added `Pagan` correctly after `Lanka`.

> **Sub-polity views:** `regions/straits-archipelago/kedah-bujang.md` etc.; `regions/mainland-thailand-laos/champa-*.md` — bypasses collapsing 1700y gaps.
> See `regions/gandhara/timeline.md`, `regions/rome-byzantium/timeline.md`, `regions/persia/timeline.md` for dated rows. `status: draft` until audit #4 completes.

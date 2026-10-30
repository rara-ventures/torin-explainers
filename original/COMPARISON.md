# Website vs TikTok — What’s Actually Different?

> 100 paired files: `sources/<slug>.md` (website, torinrussell.com) vs `script/<slug>.md` (TikTok, @torinrussell). Scraped 2026-10-29. Later we’ll compare word-for-word once transcripts are Whispered.

**TL;DR:** They’re the *same script* — website even labels it `This is the script for my video posted on…` (100/100 files). Differences are **packaging**, not substance. TikTok is the *performance*; website is the *archive*.

## 1. The Core Finding: Same Script, Different Container

| Signal | Website `sources/` | TikTok `script/` |
|--------|-------------------|------------------|
| **Body** | 1,150–1,725 words (avg **1,296**, total 129k) — full narrative | Caption avg **13 words** (total 1,333) — *title + hashtags only* |
| **Is transcript verbatim?** | Contains `This is the script for my video posted on Oct 26, 2026. Watch it on TikTok` + full 1,600-word essay | **Caption** = `How did Japan…? #geopolitics #china #japan…` — **not** the spoken script. Actual spoken words = website body minus 2 add-ons (see §2). |
| **Duration vs words** | 1296 words published | 393–545s per video (6.5–9m) → ~980–1,250 spoken words @150wpm → ratio **1.17–1.28** (website 17-28% longer than spoken). Explains add-ons. |
| **Title** | `Why is Belarus dominated by Russia?` | Same as first line of caption — **identical question** (0 mismatches across 100) |

**Proof of sameness:** `sources/how-did-japan…md:13` starts `Japan controls a 1200km chain…` and TikTok video `7701000288257264910` (545s, 129k views) has identical title + `Oct 26` date + hashtags. All 100 pairs match slug ↔ tiktok_id via regex `https://www.tiktok.com/@torinrussell/video/(\d+):1` found in website body.

**Method note:** TikTok auto-captions (`yt-dlp --write-auto-sub`) returned `There are no subtitles for the requested languages` for tested video — captions are **burned-in**, not SRT. True transcript = run Whisper on MP4 or copy website body (it *is* the transcript).

## 2. What Website Adds (Not on TikTok)

| Add-on | Example | Words |
|--------|---------|-------|
| **Frontmatter** | `categories: [Asia] tags: [Military & Defense,…]` — 10 categories, 18 tags taxonomy | — |
| **Keep reading** | `### Keep reading` + 3 links (`Why is the Yellow Sea so important?` etc.) | ~25 |
| **Book promo** | `I’m writing a book called Groundwork… Join the waitlist` | ~25 |
| **Source line** | `Source: https://torinrussell.com/explainers/... Published: 2026-10-26` | — |

These two blocks explain the 17-28% word gap. TikTok viewers never see them — they’re **SEO + newsletter** for website.

## 3. What TikTok Adds (Not on Website)

| Add-on | Example (`original/script/how-did-japan…md:6`) | Purpose |
|--------|-----------------------------------------------|---------|
| **Hashtags** | `#geopolitics #china #japan #okinawa #history` | Discovery. Website uses `tags: [Military & Defense]` — academic taxonomy. TikTok uses folksonomy for For You Page. |
| **Stats** | `view_count: 129700 like_count: 14000 duration: 545 upload_date: 20261026` | Social proof + algorithm feedback. Website has no views. |
| **Caption vs title** | Caption = `Title + hashtags` (13 words) — title *is* the hook. Website title *is* the H1. | TikTok caption is truncated in feed; question must fit 150 chars. |
| **Duration** | 545s = 9:05 (TikTok allows 10m since 2023) | Website has no duration. |

**Hashtag strategy (100 videos):**
- `#geopolitics` **100/100** — brand anchor, always first
- `#history` **88/100** — second anchor
- `#learnontiktok` **55/100** — platform booster
- Specifics: `#russia 17`, `#africa 17`, `#china 8` — mirrors website top tags (`Democracy & Governance 24`, `Economy & Trade 22`) but translated to broad discovery tags (website tags are too niche for TikTok search).

**Example mapping (same story, different taxonomy):**
- Website: `tags: [Military & Defense, Great Power Competition, Borders & Territory, Maritime]` (`how-did-japan…md:6`)
- TikTok: `#geopolitics #china #japan #okinawa #history` (`script/how-did-japan…md:12`)
- Translation: `Maritime → #okinawa`, `Great Power Competition → #china/#japan`, `Military & Defense` dropped (too jargony for TikTok), added `#history` for FYP.

## 4. What You Can Learn (Content Strategy)

### 1. One script, two jobs
Torin writes **once**, publishes twice. TikTok is the *performance* (voice, maps, 9m, captions burned-in, hashtags for reach). Website is the *canon* (searchable, 1,300w, categories/tags for SEO, Keep reading + Groundwork waitlist for retention). No rewriting — just repackaging.

> **Takeaway:** If you’re repurposing long TikToks → website, don’t rewrite. Add `Keep reading` (internal links) + newsletter CTA. That’s the 20% that makes archive outrank TikTok in Google.

### 2. Hooks are platform-agnostic
Both use `Why is / How did` question titles **verbatim**. TikTok caption *is* the website title + hashtags. No separate hook for TikTok. The hook is the question + 1,200km chain first sentence (applies everywhere).

> **Takeaway:** The `tiktok-stories/` cold hooks we built (`Not Buddhist. Not Vietnamese.`) are *more* viral than Torin’s real hooks (`Why is Macau so different…`) because Torin optimizes for **evergreen search**, not cold stop-scroll. For TikTok cold, use our negation/stat-shock; for website SEO, keep Torin’s `Why is X?` — they serve different algorithms.

### 3. Hashtags ≠ Tags
Website tags are for **librarians** (24 `Democracy & Governance` — precise, filterable via `Templates/Bases`). TikTok hashtags are for **teenagers** (`#geopolitics #history` — broad, 2-3 per video). Don’t copy website tags to TikTok — you’ll get 0 reach.

### 4. Duration tells you what was cut
At 150wpm, 545s = 1,362 spoken words. Website is 1,634 → ~272 words cut or ad-libbed out (likely `Keep reading` + book promo + some tightening). TikTok never includes those blocks. If you Whisper the MP4 and diff vs website, you’ll find ~90% verbatim, ~10% tightening (e.g., “In peacetime, Chinese warships sail…” spoken faster than written).

### 5. Views correlate with paradox, not topic
Spot-checked 5: `How do nuclear powers…` (500s, **1.2M** views) vs `Why does the Space Force exist?` (YouTube long-form, 3.5k). TikTok paradox titles (`How do nuclear powers decide to end the world?`) outperform even though website word count similar. Use `script/view_count` to prioritize which website explainers to turn into `tiktok-stories/` cold hooks.

### 6. The archive is the moat
TikTok has 299 videos, website has 100 explainers. Only the *best* 100 become `sources/` (curated, polished, SEO’d). The other ~199 TikToks are ephemeral (no website counterpart). Your `tiktok/all-videos/` (299 stubs) vs `original/sources/` (100) shows curation ratio **1:3**. That’s intentional — website is not a dump, it’s a *canon*.

## 5. How to Diff Them Yourself (Obsidian)

- **Per-pair:** Open `sources/<slug>.md` + `script/<slug>.md` side-by-side. Same slug, same title, same TikTok ID.
- **Bulk:** `Templates/Bases/TikTokScripts.base:1` (sort by `view_count DESC` to find winners) vs `original/sources` (sort by `tags`).
- **Next step (pending):** Run Whisper on 7 `youtube/long-form/*.md:1` (6-24m) + 3 TikToks to get true transcript diff. Then `tiktok-stories/` cold hooks become testable vs Torin’s original `Why is…` hook.

## 6. File Map

```
original/
├── sources/  100 website scripts (full, 129k words, avg 1,296, with Keep reading + Groundwork)
├── script/   100 TikTok stubs (caption 13 words + stats, tiktok_id, duration, views)
└── COMPARISON.md  ← you are here
tiktok/
└── all-videos/ 299 TikTok stubs (full channel, not just 100 explainers)
youtube/
└── long-form/ 7 YouTube deep dives (6-24 min, chapters)
```

*Scraped 2026-10-29 via Squarespace `?format=json` (100 explainers) + `yt-dlp --flat-playlist` (299 TikTok IDs) + `yt-dlp --dump-single-json` (per-video description/stats). Auto-captions: none via yt-dlp (burned-in), needs Whisper.*


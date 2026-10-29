---
categories: "[[TikTok Scripts]]"
created: 2026-10-29
---

# TikTok Scripts — Actual (vs Website)

> 100 TikTok caption stubs for `torinrussell` — matched 1:1 to `../sources/` website scripts. For later comparison TikTok vs website content.

**Website:** `../sources/` = full scripts as published on torinrussell.com (HTML → Markdown, 100 files)
**TikTok:** `script/` = actual TikTok metadata per video (this folder, 100 files) — caption, view/like, duration, ID

Each pair shares `slug` (e.g., `why-is-belarus-dominated-by-russia.md`):

| Website | TikTok | Compare |
|---------|--------|---------|
| `../sources/<slug>.md` | `script/<slug>.md` | Diff `description` vs full body, check hook trimming, hashtags, duration |

**Fetch:** `yt-dlp --skip-download --dump-single-json https://www.tiktok.com/@torinrussell/video/<id>` → `description` (caption), `view_count`, `like_count`, `duration`, `upload_date`. Full transcript via `--write-auto-sub --sub-lang en`.

**Status:** 100/100 scraped 2026-10-29 (yt-dlp 2026.10.26, 1.5s delay, 1 retry for Belarus). 

**Next:** Run Whisper or yt-dlp auto-sub to fill `## TikTok Auto-Captions` then diff vs website script.

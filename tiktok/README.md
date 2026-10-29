---
categories: "[[TikTok All]]"
created: 2026-10-29
---

# TikTok — Torin Russell

> Full channel scrape. Website has 100 explainers; TikTok has 299 videos (299 scraped 2026-10-29 via yt-dlp flat-playlist, no cookies).

- **All videos (299):** [`all-videos/README.md`](./all-videos/README.md) — table + per-video stubs
- **Scraper:** [`scrape.py`](./scrape.py) — uses yt-dlp (and TikTokApi fallback) — see Python libraries below
- **YouTube long-form:** [`../youtube/long-form/README.md`](../youtube/long-form/README.md) — 7 videos

**Obsidian:** `Categories/TikTok All` → `Templates/Bases/TikTokAll.base`

**Python libraries that can scrape all @torinrussell (from subagents):**

| Library | Stars | How | Full profile |
|---------|-------|-----|--------------|
| `davidteather/TikTok-Api` | 6.7k | `TikTokApi` + Playwright + ms_token — `api.user("torinrussell").videos(count=1000)` | YES |
| `yt-dlp/yt-dlp` | 204k | `yt-dlp "https://www.tiktok.com/@torinrussell"` — secUid + cursor | YES (tested 299) |
| `Evil0ctal/Douyin_TikTok_Download_API` | 16.9k | Docker + `a_bogus`/`X-Bogus` + identity pool | YES |
| `JoeanAmier/TikTokDownloader` | 17k | `curl_cffi` + X-Bogus/X-Gnarly — `tab="post"` | YES |

**Quick start (tested):**
```bash
pip install TikTokApi && python -m playwright install
# or
yt-dlp --flat-playlist --print "%(id)s" "https://www.tiktok.com/@torinrussell" | wc -l  # → 299
```

See `../tiktok-stories/` for 7 cold-hook stories derived from these.

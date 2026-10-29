"""
Scrape all TikTok videos from @torinrussell
Uses yt-dlp (primary, no browser needed) + TikTokApi fallback (Playwright + ms_token)
Tested 2026-10-29: yt-dlp flat-playlist → 299 videos (no cookies)
"""
import subprocess, json, os, sys

def via_ytdlp(username="torinrussell"):
    """Primary: yt-dlp flat-playlist (no cookies needed for @torinrussell, 299 found)"""
    url = f"https://www.tiktok.com/@{username}"
    cmd = ["python3", "-m", "yt_dlp", "--flat-playlist", "--print", "%(id)s|%(title)s|%(view_count)s|%(duration)s", url]
    out = subprocess.check_output(cmd, text=True)
    videos = []
    for line in out.splitlines():
        if "|" in line and not line.startswith("WARNING"):
            parts = line.split("|")
            if len(parts) >= 4:
                videos.append({"id": parts[0], "title": parts[1], "views": parts[2], "duration": parts[3]})
    return videos

def via_tiktokapi(username="torinrussell", ms_token=None):
    """Fallback: davidteather/TikTok-Api (needs ms_token from cookies)"""
    import asyncio
    from TikTokApi import TikTokApi

    async def _run():
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[ms_token] if ms_token else [None], num_sessions=1, sleep_after=1)
            user = api.user(username=username)
            videos = []
            async for v in user.videos(count=1000):
                d = v.as_dict
                videos.append(d)
                if len(videos) % 50 == 0:
                    print(f"Fetched {len(videos)}...")
            return videos
    return asyncio.run(_run())

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Scrape @torinrussell TikTok")
    p.add_argument("--limit", type=int, default=0, help="0 = all")
    p.add_argument("--out", default="tiktok_all.json")
    p.add_argument("--method", choices=["ytdlp","tiktokapi"], default="ytdlp")
    args = p.parse_args()

    if args.method == "ytdlp":
        vids = via_ytdlp()
        if args.limit:
            vids = vids[:args.limit]
        print(f"Found {len(vids)} videos via yt-dlp")
        json.dump(vids, open(args.out,"w",encoding="utf-8"), indent=2)
        print(f"Saved to {args.out}")
    else:
        ms = os.environ.get("ms_token")
        vids = via_tiktokapi(ms_token=ms)
        print(f"Found {len(vids)} via TikTokApi")
        json.dump(vids, open(args.out,"w"), indent=2)

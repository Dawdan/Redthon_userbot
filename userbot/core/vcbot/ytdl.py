# Red - UserBot
# Copyright (c) 2022 Redthon_USERBOT
# Credits: @RedThon || https://github.com/RedThon
#
# This file is a part of < https://github.com/RedThon/Redthon_USERBOT/ >
# t.me/RedThon & t.me/MSS3G

from youtubesearchpython import VideosSearch

from userbot import LOGS
from userbot.helpers import bash


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = data["thumbnails"][0]["url"]
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        LOGS.info(str(e))
        return 0


async def ytdl(link: str):
    stdout, stderr = await bash(
        f'yt-dlp -g -f "best[height<=?720][width<=?1280]" {link}'
    )
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr

import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 10)]
        for finish in asyncio.as_completed(fetchers):
            print(await finish)


asyncio.run(main())

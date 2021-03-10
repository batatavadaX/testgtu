import aiohttp
import aiofiles
import asyncio
import os
import uvloop
from datetime import datetime
from mygtu import PATH, gf
from tqdm import tqdm

urls = gf.gather_url()

def check_path(url):
    if "uploads" in url:
        path = PATH + url.split("/uploads/")[1].replace("/", "-")
    else:
        path = url.split("//")[1].replace("/", "-")
    return path

async def downloader(url):
    async with aiofiles.open(check_path(url), 'wb') as mad:
          await mad.write(await fetch(url))

async def fetch(url):
    async with aiohttp.request("GET", url) as r:
        return await r.read()

async def main(urls):
    for url in urls:
        le_n = len(urls)
        start = datetime.now()
        await downloader(url),
        end = datetime.now()
        fin = (end - start)
        for i in tqdm(range(100), unit="KB"):
            pass
    print(f"downloaded in [{(le_n * fin)}]")
   
async def download(urls):
    await main((urls))

uvloop.install()
asyncio.run(download(urls))

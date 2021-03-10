import aiohttp
import aiofiles
import asyncio
from datetime import datetime
from mygtu import PATH, gf
from tqdm import tqdm

urls = gf.gather_url()

async def lol(url):
  async with aiohttp.request("GET", url) as res:
    return int(res.headers.get('content-length', 0))

async def downloader(url):
    async with aiohttp.request("GET", url) as r:
        if "uploads" in url:
            path = PATH + url.split("/uploads/")[1].replace("/", "-")
        else:
            path = url.split("//")[1].replace("/", "-")
        async with aiofiles.open(path, 'wb') as mad:
          await mad.write(await r.read())

async def main(urls):
    
    for url in urls:
        le_n = len(urls)
        start = datetime.now()
        await downloader(url),
        end = datetime.now()
        fin = (end - start)
        for i in tqdm(range(100)):
            pass
    print(f"downloaded in [{(le_n * fin)}]")
   
async def download(urls):
    await main((urls))

asyncio.run(download(urls))

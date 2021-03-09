import aiohttp
import aiofiles
import asyncio

PATH = 'downloads'
urls = ['https://www.gtu.ac.in/uploads/S2020/BE/3110006.pdf', 'https://www.gtu.ac.in/uploads/S2020/BE/3110003.pdf']
async def downloader(url):
    try:
        async with aiohttp.request("GET", url) as response:
            return response.status
            if response.status==200:
                path = PATH + url.split("/uploads/")[1].replace("/", "-")
                async with aiofiles.open(path, 'wb') as mad:
                    await mad.write(await response.read())

    except Exception:
        print("URL Broken:", url)

async def main(loop, urls):
    task = [downloader(url) for url in urls]
    await asyncio.gather(*task)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop) 

def download(urls):
    loop.run_until_complete(main(loop, urls))

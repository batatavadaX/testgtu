import asyncio
import aiohttp
import aiofiles
import os
from datetime import datetime 
from .gtu import logic
from .utils.profile import *
from .utils.constants import PATH

gf = logic()

class downloader():
    def __init__():
        if not os.path.exists(PATH):
            os.mkdir(PATH)
    
    async def download(urls):
        for url in urls:
            path = PATH + url.split("/uploads/")[1].replace("/", "-")
            start = datetime.now()
            async with aiohttp.request("GET", url) as response:
                read = await response.read()
                await asyncio.sleep(2)
            async with aiofiles.open(path, 'wb') as f:
                await f.write(read)
            await f.close()
            await asyncio.sleep(2)
            end = datetime.now()

        le_n = len(urls)   
        info = f'''
        {profile.__logo__}
        Total Files : {le_n}\n
        Total Time : [{(le_n * (end - start))}]\n
        Path : {PATH}\n
        __author__ : {profile.__author__}\n
        __version__ : {profile.__version__}\n
        [{gf.current(strf="%m/%d/%Y, %H:%M:%S")}]
        '''
        with open(
            PATH+"info.txt", "w") as w:
                w.write(info)
        w.close()
        print(info)

import asyncio
import aiohttp
import aiofiles
import os
from datetime import datetime 
from .utils.time import time
from .utils.profile import __logo__, __info__, __version__
from .utils.constants import PATH

async def download(urls):


    if not os.path.exists(PATH):
        os.mkdir(PATH)
        print("creating {PATH}")
    else:
        print("found path {PATH}")

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
        fin = (end - start)
        le_n = len(urls)
        info = f'''
        {__logo__}
        Total Files : {le_n} 
        Total Time : [{(le_n * fin)}]
        Path : {PATH}
        info : {__info__}
        version: {__version__}
        [{time.current(strf="%m/%d/%Y, %H:%M:%S")}]
        '''
        with open(PATH+"info.txt", "w") as w:
            w.write(info)
        w.close()

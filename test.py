from mygtu import dl, gf
import asyncio
import uvloop

async def main():
    db = gf.database()
    urls = gf.gather_url(db)
    await dl.download(urls)

uvloop.install()
asyncio.run(main())

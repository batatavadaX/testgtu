from mygtu import dl, logic
import asyncio

async def main():
    gf = logic("downloads/k.json")
    db = gf.database()
    urls = gf.gather_url(db)
    await dl.download(urls)

asyncio.run(main())

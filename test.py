from mygtu import dl, mad
import asyncio

async def main():
    gf = mad(path="testgtu/mygtu/database/subject_code.json")
    db = gf.database()
    urls = gf.gather_url(db)
    await dl.download(urls)

asyncio.run(main())

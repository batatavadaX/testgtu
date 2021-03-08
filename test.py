from mygtu import dl, logic

async def k():
    gf = logic()
    db = gf.database("downloads/k.json")
    urls = gf.gather_url(db)
    await dl.download(urls)

await k()

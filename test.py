from mygtu import dl, logic

async def k():
    gf = logic("downloads/k.json")
    db = gf.database()
    urls = gf.gather_url(db)
    await dl.download(urls)

await k()

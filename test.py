from mygtu import dl, logic

gf = logic()

db = gf.database()
urls = gf.gather_url(db)
await dl.download(urls)

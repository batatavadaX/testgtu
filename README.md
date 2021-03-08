# testgtu

you can use an userbot and run

```py
pip3 install https://github.com/batatavadaX@gtu-z
```

default values set to ic first year

```py
from mygtu import dl, gf
urls = gf.gather_url()
await dl.download(urls)
```

you can pass values

```py
from mygtu import dl, mad
gf = mad(path="path/to_json.json")
db = gf.database()
urls = mad.gather_url(db)
await dl.download(urls)
```

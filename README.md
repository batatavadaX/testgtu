# mygtu

`download gtu old papers with async downloader
 on average you can download 20 pdf of ~250KB in 2 min`


```py
pip3 install --no-cache git+https://github.com/batatavadaX/testgtu@gtu-z
```

default values set to ic first year

```py
from mygtu import dl, gf
urls = gf.gather_url()
await dl.download(urls)

# will download all the old papers of ic branch.
```

you can pass values

here's json example

```json
{
    "IC":{
        "FIRST_YEAR":[
            "3110006",
            "3110003",
            "3110005",
            "3110007",
            "3110014"
        ]
    }
}
```

# example.
```py
from mygtu import dl, mad
import asyncio

async def main():
    gf = mad(
    path="path/to_json.json", 
    branch="IC", 
    year="FIRST_YEAR",
    course="BE"
    )
    db = gf.database()
    urls = gf.gather_url(db)
    await dl.download(urls)

asyncio.run(main())
```

# testgtu

you can use an userbot and run

```py
pip3 install --no-cache git+https://github.com/batatavadaX/testgtu@gtu-z
```

default values set to ic first year

```py
from mygtu import dl, gf
urls = gf.gather_url()
await dl.download(urls)
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

(this examples are for all ready running loops check test.py)
```py
from mygtu import dl, mad
gf = mad(
    path="path/to_json.json", 
    branch="IC", 
    year="FIRST_YEAR",
    course="BE"
    )
db = gf.database()
urls = mad.gather_url(db)
await dl.download(urls)
```

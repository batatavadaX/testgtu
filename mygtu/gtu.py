import os
import pytz
import ujson
import itertools
from datetime import datetime
from .utils import y_list
from .utils.constants import DIR


class logic:
    def __init__(
        self,
        *,
        branch :str = "IC",
        year :str = "FIRST_YEAR",
        url :str = "https://www.gtu.ac.in/uploads/",
        path :str = (DIR / 'database/subject_code.json'),
        course :str = "BE",
        extension :list = ".pdf"
    ) -> None:
        self._branch = branch
        self._year = year
        self._course = course
        self._uri = url
        self._path = path
        self._extension = extension
        
    
    def database(self):
        with open(self.path, "r") as k:
            data = ujson.load(k)
        return data[f"{self.branch}"][f"{self.year}"]
     
    def fetch_uri(self):
        base = self.uri
        course = self.course
        a = y_list[0]
        b = y_list[1]
        c = y_list[2]
        fetch = [
            f"{base}S{a}/{course}",
            f"{base}S{b}/{course}", 
            f"{base}W{b}/{course}", 
            f"{base}W{c}/{course}"
        ]
        return fetch  
        

    def gather_url(
        self, 
        db: Optional[str] = None,
    ):
        op = ['.pdf']
        db = self.database()
        x = self.fetch_uri()
        z = list(itertools.product(x,db))
        p = list(["/".join(all) for all in z])
        q = list(itertools.product(p, op))
        return list(["".join(all) for all in q])
    
    

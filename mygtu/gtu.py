import os
import pytz
import ujson
import itertools
from datetime import datetime

O_O = os.path.join(os.path.dirname(os.path.abspath(__file__)),'database/subject_code.json'))

class logic:
    def __init__(
        self,
        branch = "IC",
        year = "FIRST_YEAR",
        url = "https://www.gtu.ac.in/uploads/",
        path = O_O
        course = "BE",
        extension = ".pdf"
    ):
        self.branch = str(branch)
        self.year = str(year)
        self.course = str(course)
        self.uri = str(url)
        self.path = str(path)
        self.extension = list(extension)

    @staticmethod
    def current(zone="Asia/Kolkata"):
        return datetime.now(pytz.timezone(zone)).strftime("%Y")

    @staticmethod
    def year():
        new = []
        for i in range(1, 4):
            new.append(int(logic.current()) - i)
        return new

    def database(self):
        k = open(self.path, "r")
        data = ujson.load(k)
        return data[f"{self.branch}"][f"{self.year}"]

    def fetch_uri(self):
        base = self.uri
        course = self.course
        a = logic.year()[0]
        b = logic.year()[1]
        c = logic.year()[2]
        fetch = [
            f"{base}S{a}/{course}",
            f"{base}S{b}/{course}", 
            f"{base}W{b}/{course}", 
            f"{base}W{c}/{course}"
        ]
        return fetch
        

    def gather_url(self, db):
        op = ['.pdf']
        db = self.database()
        x = self.fetch_uri()
        z = list(itertools.product(x,db))
        p = list(["/".join(all) for all in z])
        q = list(itertools.product(p, op))
        return list(["".join(all) for all in q])
    

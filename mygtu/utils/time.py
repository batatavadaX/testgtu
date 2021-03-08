from datetime import datetime 
import pytz

class time:
    def __init__():
        return "lol"
    @staticmethod 
    def current(zone='Asia/Kolkata', strf='%Y'): 
        return datetime.now( 
            pytz.timezone( 
                zone 
                ) 
            ).strftime(
                strf
            )

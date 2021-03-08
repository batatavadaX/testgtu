from datetime import datetime 
import pytz

def current(zone='Asia/Kolkata', strf='%Y'): 
    return datetime.now( 
        pytz.timezone( 
            zone 
            ) 
        ).strftime(
            strf
        )

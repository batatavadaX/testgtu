from datetime import datetime 
import pytz

class time:
    @staticmethod 
    def current(
        str: zone='Asia/Kolkata', 
        str: strf='%Y'
    ) -> int: 
        return datetime.now( 
            pytz.timezone( 
                zone 
                ) 
            ).strftime(
                strf
            )

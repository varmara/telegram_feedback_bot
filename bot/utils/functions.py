import datetime
import pytz  

def admin_time(admin_time_zone: str = "Europe/Moscow") -> str:
    now = datetime.datetime.now(pytz.timezone(admin_time_zone))
    return now.strftime("%d.%m.%Y %H:%M:%S")
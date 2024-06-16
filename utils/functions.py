import datetime
import pytz  

def moscow_time():
    now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    return now.strftime("%d.%m.%Y %H:%M:%S")+" (МСК)"
from datetime import datetime, timedelta
from pytz import timezone
import calendar

myanmar_timezone = "Asia/Yangon"

def get_cur_datetime():
    return datetime.now(timezone(myanmar_timezone))

def format_datetime24(now: datetime):
    return now.strftime('%Y-%m-%d %H:%M:%S')

def format_datetime(now: datetime):
    return now.strftime('%Y-%m-%d %I:%M:%S')

def get_date():
    dt = get_cur_datetime()
    return {
        'day': dt.day,
        'month': dt.month,
        'year': dt.year,
        'hour': dt.hour,
        'minute': dt.minute,
        'date': dt.strftime('%Y-%m-%d'),
        'datetime24': dt.strftime('%Y-%m-%d %H:%M:%S'),
        'datetime': dt.strftime('%Y-%m-%d %I:%M:%S'),
        'weekday': calendar.day_name[dt.weekday()]
    }

def get_start_date():
    now = get_cur_datetime() + timedelta(seconds=5)
    return format_datetime24(now)

def get_first_end_date() -> str:
    return get_date().get('date') + ' 12:03:00'

def get_second_end_date() -> str:
    return get_date().get('date') + ' 16:32:00'
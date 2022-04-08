from datetime import datetime
from pytz import timezone

myanmar_timezone = 'Asia/Yangon'

def get_cur_datetime():
    return datetime.now(timezone(myanmar_timezone))

def format_datetime24(now: datetime):
    return now.strftime('%Y-%m-%d %H:%M:%S')

def format_datetime(now: datetime):
    return now.strftime('%Y-%m-%d %I:%M:%S')


if __name__ == '__main__':
  print('Tick the time is', format_datetime(get_cur_datetime()))
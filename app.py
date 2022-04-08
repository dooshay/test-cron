from datetime import timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from date_utils import get_date, myanmar_timezone
import logging

count = 0

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

sched = BackgroundScheduler(timezone=myanmar_timezone)

def tick():
    print('Tick! The time is: %s' % get_date().get('datetime'))
    count += 1
    if count == 5:
      sched.remove_job('my_job')
      sched.shutdown()

if __name__ == '__main__':
  
  # now = get_date().get('date') + timedelta(seconds=5)

  sched.add_job(tick, 'interval', seconds=5, id='my_job')

  try:
    sched.start()
  except (KeyboardInterrupt, SystemExit):
    pass
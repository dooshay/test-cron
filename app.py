# from datetime import timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from date_utils import get_date, myanmar_timezone
import logging
import time
import os

def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.CRITICAL)

def tick():
  global count
  print('Tick! The time is: %s' % get_date().get('datetime'), flush=True)
  time.sleep(2)
  count += 1
  if count == 5:
    sched.remove_job('my_job')
    os._exit(0)


if __name__ == '__main__':
  count = 0

  sched = BlockingScheduler(timezone=myanmar_timezone)

  sched.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

  sched.add_job(tick, 'interval', seconds=5, id='my_job', timezone=myanmar_timezone)

  try:
    sched.start()
  except (KeyboardInterrupt, SystemExit):
    print('Something went wrong.')
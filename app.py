from datetime import timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from date_utils import get_date, myanmar_timezone
# import logging
import time

# logger = logging.getLogger(__name__)
count = 0

# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)


def tick():
    print('Tick! The time is: %s', get_date().get('datetime'))
    time.sleep(2)
    count += 1
    if count == 5:
      sched.remove_job('my_job')
      sched.shutdown()


if __name__ == '__main__':

  sched = BackgroundScheduler(timezone=myanmar_timezone)

  sched.add_job(tick, 'interval', seconds=5, id='my_job', timezone=myanmar_timezone)

  try:
    sched.start()
  except (KeyboardInterrupt, SystemExit):
    print('Something went wrong.')
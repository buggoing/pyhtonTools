import time
import datetime


timestampNow = time.strftime("%Y%m%d%H%M%S")

now = datetime.now()
nowyymmddhhmmss = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)

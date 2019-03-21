import time
import datetime


timestampNow = time.strftime("%Y%m%d%H%M%S")

now = datetime.datetime.now()
# 20181119105211
nowyymmddhhmmss = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
nowyymmddhhmmss = dt.strftime("%Y%m%d%H%M%S")

dt = datetime.datetime.now()
# 20181119105211_79179
timestampNow = dt.strftime("%Y%m%d%H%M%S") + '_' + str(dt.microsecond)
yymmddhhmmss_mss = timestampNow
print yymmddhhmmss_mss
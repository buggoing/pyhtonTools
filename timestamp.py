import sys
import time

def timestammpToString(timestamp):
  localTime = time.localtime(timestamp)
  timeString = time.strftime('%Y-%m-%d %H:%M:%S', localTime)
  return timeString

def stringToTimestamp(timesString):
  '''2011-09-28 10:00:00'''
  timestamp = time.mktime(time.strptime(timesString, '%Y-%m-%d %H:%M:%S'))
  return timestamp

def calculateTimeDiffDays(startTimeString, endTimeString):
    startTime = datetime.datetime.strptime(startTimeString, "%Y-%m-%d")
    endTime = datetime.datetime.strptime(endTimeString, "%Y-%m-%d")
    # print startTime
    # print endTime
    diff = endTime - startTime
    # print diff.days
    # print dir(diff)
    return diff.days

if __name__ == '__main__':
  paramer = sys.argv[2]
  opcode = sys.argv[1]
  if opcode == '0':
    print(timestammpToString(float(paramer)))
  elif opcode == '1':
    print(stringToTimestamp(paramer))

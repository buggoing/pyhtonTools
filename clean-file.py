
import os
import glob
import time
import datetime
import gbox_params

logpath = "./log"

def calculateTimeDiffDays(startTimeString, endTimeString):
    startTime = datetime.datetime.strptime(startTimeString, "%Y-%m-%d")
    endTime = datetime.datetime.strptime(endTimeString, "%Y-%m-%d")
    # print startTime
    # print endTime
    diff = endTime - startTime
    # print diff.days
    # print dir(diff)
    return diff.days

def cleanFile(path, day=7):
    allFiles = glob.glob(path + '/*')
    for fullFilepath in allFiles:
        modifyTime = os.path.getmtime(fullFilepath)
        modifyTime = time.localtime(modifyTime)
        fileModifiedDate = time.strftime('%Y-%m-%d', modifyTime)
        print fullFilepath, fileModifiedDate
        currentTimeString = time.strftime("%Y-%m-%d")
        diffDays = calculateTimeDiffDays(fileModifiedDate, currentTimeString)
        if diffDays > day:
            cmd = 'rm ' + fullFilepath
            os.system(cmd)
            print 'remove: ' + fullFilepath

cleanFile(logpath, 10)

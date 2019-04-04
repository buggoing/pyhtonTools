#coding:utf8
import time
import sys
import logging
import logging.handlers
import os
import json

reload(sys) 
sys.setdefaultencoding("utf-8")

dir_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists('./logs'):
    os.mkdir('./logs')

logpath = os.path.join(dir_path, "logs/myapp.log")
testlogpath = os.path.join(dir_path, "logs/test.log")
 

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s-%(filename)s-%(funcName)s-line:%(lineno)d-%(levelname)s---%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',)

formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s line:%(lineno)d %(levelname)s---%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')  #定义该handler格式

mylogger = logging.getLogger('myapp')
mylogger.setLevel(logging.INFO)

testlogger = logging.getLogger('testlog')
testlogger.setLevel(logging.INFO)

trhandler = logging.handlers.TimedRotatingFileHandler(logpath, when='s', encoding='utf-8', interval=5, backupCount=5)
trhandler.suffix = "%Y-%m-%d_%H:%M:%S.log"
# trhandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
trhandler.setLevel(logging.INFO)
trhandler.setFormatter(formatter)

rthandler = logging.handlers.RotatingFileHandler(logpath, maxBytes=10*1024*1024, backupCount=50)
rthandler.setLevel(logging.INFO)
rthandler.setFormatter(formatter)

testRthandler = logging.handlers.RotatingFileHandler(testlogpath, maxBytes=10*1024*1024, backupCount=50)
testRthandler.setLevel(logging.INFO)
testRthandler.setFormatter(formatter)

mylogger.addHandler(trhandler)

def test():
    res = {'res': {'msg': u'证券行业', 'code': 0}, 'data': {u'code': 0}}
    res = json.dumps(res, encoding="UTF-8", ensure_ascii=False)
    while True:
        mylogger.info(u'中文')
        mylogger.info(str(u'中文2'))
        mylogger.info(res)
        # mylogger.info("返回code不是200")
        time.sleep(1)

if __name__ == '__main__':
    test()


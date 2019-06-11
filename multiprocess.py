import time
import multiprocessing
from multiprocessing import Process, Queue, Manager

CPU_NUM = multiprocessing.cpu_count()

class Task():
    def __init__(self, i):
        self.num = i

    def work(self, i):
        while True:
            time.sleep(2)
            print('working: ', i)
    
    def start(self):
        self.proc = Process(target=self.work, args=(self.num,))
        self.proc.start()
    

# taskList = []
# for i in range(CPU_NUM):
#     task = Task(i)
#     task.start()
#     taskList.append(task)


container = Queue(maxsize=10)


def processPro(gvalue):
    while True:
        if container.full():
            
            ele = container.get()
            print('pro', ele)
        current = time.time()
        container.put(current)
        gvalue['time'] = current
        time.sleep(0.1)


def processCon(gvalue, no):
    while True:
        ele = container.get()
        print(no, ele)
        print("{no}, current: {current}".format(no=no, current=gvalue['time']))
        time.sleep(1)

def main():
    gValue = Manager().dict({'time': 0})
    pro = Process(target=processPro, args=(gValue,))
    pro.start()

    for i in range(5):
        pro = Process(target=processCon, args=(gValue, i))
        pro.start()
    
    while True:
        print('main: ', gValue['time'])
        time.sleep(2)


main()
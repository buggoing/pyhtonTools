import time
import multiprocessing
from multiprocessing import Process, Queue

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
    

taskList = []
for i in range(CPU_NUM):
    task = Task(i)
    task.start()
    taskList.append(task)


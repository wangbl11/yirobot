import threading
from random import randint
import time

L=[]
lock_con=threading.Condition()
class Producer(threading.Thread):
    def run(self):
        while True:
            val=randint(0,100)
            print("生产",self.name," 添加"+str(val))
            with lock_con:
                L.append(val)
                lock_con.notify()
            time.sleep(3)

class Consumer(threading.Thread):
    def run(self):
        while True:
            with lock_con:
                if len(L)==0:
                    lock_con.wait()
                print("消费",self.name,str(L[0]))
                del L[0]
            time.sleep(0.5)



threads=[]
for i in range(5):
    threads.append(Producer())

threads.append(Consumer())

for t in threads:
    t.start()
for t in threads:
    t.join()

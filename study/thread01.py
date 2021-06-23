import time
def countdown(n):
    for i in range(n):
        print('减1')
        n-=1
        time.sleep(5)

from threading import Thread
t=Thread(target=countdown,args=(4,))
t.start()
t.join()
if t.is_alive():
    print('still ative')
else:
    print('already inactive')
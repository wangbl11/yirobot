from threading import Thread,Event
import time
def countdown(n,start_evt):
    print('countdown start...')
    start_evt.set()
    while n>0:
        print('减1')
        n-=1
        time.sleep(5)

start_evt=Event()
t=Thread(target=countdown,args=(5,start_evt,))
t.start()
start_evt.wait()
print('down?')
import time
class CountDown:
    def __init__(self):
        self._running=True
    def terminiate(self):
        self._running=False

    def run(self,n):
        while self._running and n>0:
            print('减1')
            n-=1
            time.sleep(3)
# c=CountDown()
# from threading import Thread
# t=Thread(target=c.run,args=(5,))
# t.start()
# c.terminiate()
# t.join()
import socket
class IOTask:
    def __init__(self):
        self._running=True

    def terminate(self):
        self._running=False

    def run(self,sock):
        sock.settimeout(5)
        while self._running:
            try:
                data=sock.recv(8192)
                break
            except socket.timeout:
                continue
        return

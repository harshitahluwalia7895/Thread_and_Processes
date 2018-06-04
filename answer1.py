from threading import *
import time
class myThread(Thread):
    def run(self):
        for i in range(10):
            print('Child Thread')
t=myThread()
time.sleep(5)
t.start()

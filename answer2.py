from threading import *
import time
class new(Thread):
    def run(self):
        for i in range(1,11):
            print(i)
            time.sleep(1)
t=new()
t.start()
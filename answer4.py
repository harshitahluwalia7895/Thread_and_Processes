from threading import *
import time
import math
class abc(Thread):
    def run(self):
        m = int(input('Enter the Number to be Factorial:'))
        print('The factorial of {} is '.format(m),math.factorial(m))
t=abc()
t.start()
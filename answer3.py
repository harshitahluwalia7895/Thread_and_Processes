from threading import *
import time
l=[]
print('You are Allowed to enter only 5 Elements:')
for i in range(1,6):
    m=input('Enter {} element:'.format(i))
    l.append(m)

def display(l):
    print('Displaying all elements of the list with delay: ')
    j = 0
    for i in range(2, 11, 2):
        print(l[j])
        print('Going to sleep for {} seconds'.format(i))
        time.sleep(i)
        j += 1

t = Thread(target=display, args=(l,))
t.start()
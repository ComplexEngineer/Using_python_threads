import threading as tr
import time

print("Start")

def th1():
    while True:
        print("1")
        time.sleep(1)

def th2():
    a=0
    while True:
        print(a)
        a=a+1
        time.sleep(1.5)

t1 = tr.Thread(target=th1)
t2 = tr.Thread(target=th2)

t1.start()
t2.start()

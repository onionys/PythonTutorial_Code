#!/usr/bin/env python3

from threading import Thread
from time import sleep

def thread_1():
    for i in range(10):
        sleep(2)
        print("thread 1 : running....")
    print("thread 1 : stop!!!")

    
the_thread = Thread(target = thread_1, args=())
the_thread2 = Thread(target = thread_1, args=())

the_thread.start()
the_thread2.start()

for i in range(10):
    sleep(3)
    print("\t\tmain loop running.....")
print("\t\tmain loop stop.")

#!/usr/bin/env python3


from threading import Thread
from time import sleep

system_run = 1

def do_something_func():
    while(system_run):
        sleep(1)
        print("do_something_func: running....")
    print("do_something_func: stop!!!")


if __name__ == '__main__':
    do_something_thread = Thread(target = do_something_func)
    do_something_thread.start()

    while(system_run):
        a = input()
        if a == 'a':
            system_run = 0
    

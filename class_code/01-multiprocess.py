#!/usr/bin/env python3

from multiprocessing import Process, Queue
from time import sleep


def some_loop_func():
    inf = open('proc_log.txt','w')
    for i in range(10):
        sleep(1)
        inf.write("some_proc:%d\n" % i)
    inf.close()


if __name__ == '__main__' :
    some_loop_proc = Process(target = some_loop_func)
    some_loop_proc.start()

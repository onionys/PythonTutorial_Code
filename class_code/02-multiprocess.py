#!/usr/bin/env python3

from multiprocessing import Process, Queue, current_process
from time import sleep


def some_loop_func(q):
    p = current_process()

    while True:
        sleep(1)
        if(q.empty()):
            print("%s: waiting for message ...." % p.name)
        else:
            message = q.get()
            print("%s: I got message from queue : <%s>" % (p.name, message))
            if(message == 'stop'): break

    print("some_loop_func stop!!")



if __name__ == '__main__' :
    queue_01 = Queue()

    some_loop_proc_01 = Process(name = "01", target = some_loop_func, args = (queue_01,))
    some_loop_proc_01.start()

    for i in range(2):
        sleep(2)
        print('yo man')
        queue_01.put('yo man!!')

    queue_01.put('stop')
    some_loop_proc_01.join()

    print("main loop stop!!!!")

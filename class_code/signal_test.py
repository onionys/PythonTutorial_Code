

import signal
from time import sleep

def signal_handler(signum, frame):
    print("signum: %d" % signum)
    print("You Press teh ctrl + c")


signal.signal(signal.SIGINT, signal_handler)

for i in range(10):
    sleep(2)
    print("waiting....%d" % i)

print("END")

signal.signal(signal.SIGINT, signal.SIG_DFL)

for i in range(10):
    sleep(2)
    print("waiting....%d" % i)

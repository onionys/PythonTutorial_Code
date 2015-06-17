#!/usr/bin/env python3

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

btns = [23,24]

for i in btns:
    GPIO.setup(i, GPIO.IN)


def btn_func(channel):
    print("btn is pressed %d" % channel)

GPIO.add_event_detect(btns[0], GPIO.RISING, btn_func)

for i in range(10):
    sleep(2)
    print('sleeping')

#!/usr/bin/env python3

# /boot/cmdline.txt: isolcpus=3
# taskset -c 3 ./pwmread.py

import RPi.GPIO as GPIO
import time
import os

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    print ("Hello World!")
    msg = "value: {:4d}, min: {:4d}, max: {:4d}" 
    min = 9999;
    max = -1;
    while True:
        time.sleep(0.015)
        while GPIO.input(pin) == 0:
            pass
        t = time.time()
        while GPIO.input(pin) == 1:
            pass
        diff = time.time() - t
        value = round(-15 + 1000000 * (diff))
        if value < min:
            min = value
        if value > max:
            max = value
        os.system('clear') 
        print (msg.format(value, min, max))
finally:
    GPIO.cleanup()


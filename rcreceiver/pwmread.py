#!/usr/bin/env python3

# /boot/cmdline.txt: isolcpus=3
# taskset -c 3 ./pwmread.py

import RPi.GPIO as GPIO
import time
import os
import socket

# Receiver's end
UDP_IP = "192.168.42.113"
UDP_PORT = 5005

# Sender's end
pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    print ("Hello World, this is the Johannis Crawler!")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    msg = "value: {:4d}, min: {:4d}, max: {:4d}" 
    min = 9999;
    max = -1;

    print ("Init done.")

    while True:
        time.sleep(0.015)
        while GPIO.input(pin) == 0:
            pass
        t = time.time()
        while GPIO.input(pin) == 1:
            pass
        diff = time.time() - t
        value = round(-25 + 1000000 * (diff))
        if value < min:
            min = value
        if value > max:
            max = value
        os.system('clear') 
        print (msg.format(value, min, max))

        # Send via UDP
        udpMessage = "CH1 {}".format(value)
        sock.sendto(bytes(udpMessage, 'UTF-8'), (UDP_IP, UDP_PORT))
        
finally:
    GPIO.cleanup()


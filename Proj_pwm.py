# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:18:01 2021

@author: anime
"""

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(35,GPIO.IN)
p=GPIO.PWM(35,100)
while not KeyboardInterrupt:
    p.start(10) #Motor will run at slow speed
    
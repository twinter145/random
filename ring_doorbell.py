#!/usr/bin/env python3

import time

import RPi.GPIO as io

io.setmode(io.BCM)
doorbell = 4 # Doorbell is connected to GPIO pin 4
io.setup(doorbell, io.OUT)

# Ring doorbell
io.output(doorbell, True)
time.sleep(1)
io.output(doorbell, False)

io.cleanup(doorbell)


import RPi.GPIO as GPIO 
import time
import sys

pin = 36
GPIO.setmode(GPIO.BOARD)
#Pin setup: pin = 36
GPIO.setup(pin, GPIO.OUT)
#
GPIO.out(pin, False) #on
GPIO.out(pin, True)  #off

#parse array sys.argv into time chunks 1h 30m 15s into time.sleep(seconds)
hotSec = 0
for i in sys.argv:
    #do the thing

try:

except KeyboardInterrupt:
    GPIO.cleanup()

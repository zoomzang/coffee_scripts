import RPi.GPIO as GPIO
import time

in1 = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.output(in1, False)
time.sleep(0.5)
GPIO.output(in1, True)
time.sleep(0.5)
GPIO.output(in1, False)


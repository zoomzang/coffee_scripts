import RPi.GPIO as GPIO
import time

in1 = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
#GPIO.setwarnings(False)

GPIO.output(in1, False)
time.sleep(0.5)
GPIO.output(in1, True)
time.sleep(0.5)
GPIO.output(in1, False)
time.sleep(0.5)
GPIO.output(in1, True)
time.sleep(0.5)
GPIO.output(in1, False)
time.sleep(0.5)
try:
    while True:
        GPIO.output(in1, True)
        time.sleep(60*60*1.5)
        GPIO.output(in1,False)
        time.sleep(60*60*22.5)
except KeyboardInterrupt:
    GPIO.cleanup()


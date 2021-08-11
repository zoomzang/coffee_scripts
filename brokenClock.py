import RPI.GPIO as GPIO
import time

coffeeRelay = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(coffeeRelay, GPIO.OUT)

# remember, it does not matter what the local time is, this is 
#  a broken clock and will run from start

#relay startup check
GPIO.output(coffeeRelay, True)
time.sleep(.5)
GPIO.output(coffeeRelay, False)
time.sleep(.5)
GPIO.output(coffeeRelay, True)
time.sleep(.5)
GPIO.output(coffeeRelay, False)


try: 
	while True: 
		#turn on coffee for an hour ^-^
		GPIO.output(coffeeRelay, True)
		time.sleep(60*60*1)

		#turn off Mr. Coffee for 23 hours ;-;	
		GPIO.output(coffeeRelay, False
		time.sleep(60*60*23)

#cleanup GPIO upon ctrl+c interupt --(kind of boring)
except KeyboardInterrupt:
	GPIO.cleanup()

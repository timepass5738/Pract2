import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led1= 36 #GPIO 16
led2= 38 #GPIO 20
led3= 40 # GPIO 21

GPIO.setup((led1),GPIO.OUT)
GPIO.setup((led2),GPIO.OUT)
GPIO.setup((led3),GPIO.OUT)
def pattern():
GPIO.output(led1,True)
time.sleep(1)
GPIO.output(led1,False)
GPIO.output(led2,True)
time.sleep(1)
GPIO.output(led2,False)
GPIO.output(led3,True)
time.sleep(1)
GPIO.output(led3,False)

print(&#39;Blinking LED pattern&#39;)
while True:
pattern()

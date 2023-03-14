import RPi.GPIO as GPIO
import time

LED=3
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LED, GPIO.OUT)

n=10
while n>0:
    print('HIGH')
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    print('LOW')
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)    
    n -= 1
GPIO.cleanup()
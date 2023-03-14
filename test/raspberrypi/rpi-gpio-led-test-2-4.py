import RPi.GPIO as GPIO
import time

led_pins=[2, 3, 4, 17]
GPIO.setmode(GPIO.BCM)
for i in led_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

n=10
while n>0:
    for i in led_pins:
        print(f'LED{i} is ON')
        GPIO.output(LED, GPIO.HIGH)  
        time.sleep(0.5)
        print(f'LED{i} is OFF')
        GPIO.output(LED, GPIO.LOW)    
        time.sleep(0.5)    
    n -= 1
GPIO.cleanup()
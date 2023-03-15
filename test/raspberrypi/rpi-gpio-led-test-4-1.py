import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 10)      # Pin3= GPIO2, 頻率 10 Hz

while True:
    for dc in range(5, 101, 5):   # dc=5~100 增幅為 5
        pwm.start(dc)
        sleep(0.5)
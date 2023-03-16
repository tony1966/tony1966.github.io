from gpiozero import PWMLED
from time import sleep

pwm=PWMLED(2, frequency=10)
dc=0.05
while True:
    if dc <= 1.0:
        pwm.value=dc
        dc += 0.05
    else:
        dc=0.05
    sleep(0.5)
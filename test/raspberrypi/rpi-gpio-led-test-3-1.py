from gpiozero import LED
from time import sleep

led=LED(2)
n=10
while n>0:
    print('ON')
    led.on()    
    sleep(0.5)
    print('OFF')
    led.off()    
    sleep(0.5)    
    n -= 1
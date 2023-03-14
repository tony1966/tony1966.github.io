# rpi-gpio-led-test-3-2.py
from gpiozero import LED
from time import sleep

led_pins=[2, 3, 4, 17]
leds=[]
for i in led_pins:
    leds.append(LED(i))

n=10
while n>0:
    for i in range(4):
        print(f'LED{i} is ON')
        leds[i].on()  
        sleep(0.5)
        print(f'LED{i} is OFF')
        leds[i].off()    
        sleep(0.5)    
    n -= 1
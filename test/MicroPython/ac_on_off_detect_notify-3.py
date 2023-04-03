from machine import Pin
from time import sleep

def irq_handler(pin):
    global irq_pin
    global irq_occurred
    irq_occurred=True
    irq_pin=pin

irq_occurred=False
led_pin=Pin(2, Pin.OUT)
led_pin.value(1) 
solar_pin=Pin(5, Pin.IN, Pin.PULL_UP)
solar_pin.irq(trigger=3, handler=irq_handler)

while True:
    if irq_occurred:
        sleep(0.5)
        if solar_pin.value():
            print(f'{irq_pin} 發生中斷 : 斷電')
        else:
            print(f'{irq_pin} 發生中斷 : 復電')
        led_pin.value(0)
        sleep(1)
        led_pin.value(1)
        irq_occurred=False
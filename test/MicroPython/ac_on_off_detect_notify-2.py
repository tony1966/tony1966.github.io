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
solar_pin_r=Pin(5, Pin.IN, Pin.PULL_UP)
solar_pin_r.irq(trigger=Pin.IRQ_RISING, handler=irq_handler)
solar_pin_f=Pin(4, Pin.IN, Pin.PULL_UP)
solar_pin_f.irq(trigger=Pin.IRQ_FALLING, handler=irq_handler)

while True:
    if irq_occurred:
        print(f'{irq_pin} 發生中斷')
        print(str(irq_pin))
        led_pin.value(0)
        sleep(3)
        led_pin.value(1)
        irq_occurred=False
from machine import Pin, ADC
import time

led=Pin(2, Pin.OUT)

while True:
    adc=ADC(0) 
    value=adc.read()    
    value=int(0.3*value + 0.7*adc.read());  
    luminance=round(value*100/1024)
    print(value, str(luminance) + '%') 
    if luminance < 30:      
        led.value(0)               
    elif luminance > 35: 
        led.value(1)              
    time.sleep(1)
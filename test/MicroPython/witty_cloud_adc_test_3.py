from machine import Pin, ADC
import time

led=Pin(2, Pin.OUT)    

while True:
    adc=ADC(0)  
    value=adc.read()    
    value=int(0.3*value + 0.7*adc.read());  
    print(value, str(round(value*100/1024)) + '%') 
    led.value(1)    
    time.sleep_ms(value)    
    led.value(0)    
    time.sleep_ms(value)    
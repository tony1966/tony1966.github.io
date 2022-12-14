import machine
import time

while True:
    adc=machine.ADC(0)    
    value=adc.read()           
    print(value, str(round(value*100/1024)) + '%')     
    time.sleep(1)                
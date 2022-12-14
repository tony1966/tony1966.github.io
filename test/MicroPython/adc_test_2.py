import machine
import time

while True:
    adc=machine.ADC(0)  
    value=adc.read()          
    value=0.3*value + 0.7*adc.read();    # 積分濾波
    print(value, str(round(value*100/1024)) + '%') 
    time.sleep(1)   
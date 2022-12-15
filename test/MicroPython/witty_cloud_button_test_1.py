from machine import Pin, ADC
import time

led=Pin(2, Pin.OUT)
button=Pin(4, Pin.IN)
led.value(1)  # 預設熄滅 LED

while True:
    value=button.value()
    if value:  # 1=按鈕放開
        print("按鈕狀態 :", value)
        led.value(1)
    else:      # 0=按鈕按下
        print("按鈕狀態 :", value)
        led.value(0)
from machine import Pin, ADC
import time

led=Pin(2, Pin.OUT)
button=Pin(4, Pin.IN)
led.value(1)  # 預設熄滅 LED

while True:
    if not button.value():  # 按鈕按下
        led.value(not led.value())
        while not button.value():
            pass
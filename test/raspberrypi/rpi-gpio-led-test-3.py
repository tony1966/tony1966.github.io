import RPi.GPIO as GPIO
import time

LED=3
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        print('HIGH')
        GPIO.output(LED, 1)
        time.sleep(0.5)
        print('LOW')
        GPIO.output(LED, 0)
        time.sleep(0.5)
except Exception:    # 中斷發生時不處理
    pass
     
GPIO.cleanup()
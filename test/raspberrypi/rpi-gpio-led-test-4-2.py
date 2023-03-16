import RPi.GPIO as GPIO
form time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

pwm=GPIO.PWM(3, 50) 
pwm.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            sleep(0.1)
        for dc in range(100, -1, -5):
            pwm.ChangeDutyCycle(dc)
            sleep(0.1)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()
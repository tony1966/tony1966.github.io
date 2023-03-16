from gpiozero import PWMLED
from time import sleep
import numpy as np

pwm=PWMLED(2, frequency=50)
try:
    while 1:
        for dc in np.arange(0, 1, 0.05):
            pwm.value=dc
            sleep(0.1)
        for dc in np.arange(1, 0, -0.05):
            pwm.value=dc
            sleep(0.1)
except KeyboardInterrupt:
    pass

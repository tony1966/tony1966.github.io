import xtools
from xtools import pad_zero
import ssd1306
from machine import Pin, SoftI2C

ip=xtools.connect_wifi_led()
i2c=SoftI2C(scl=Pin(22), sda=Pin(21))               
oled=ssd1306.SSD1306_I2C(128, 32, i2c)
week={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

n=0
while True:
    utc_epoch=time.mktime(time.localtime())
    Y,M,D,H,m,S,W,DY=time.localtime(utc_epoch + 28800)
    YMD=f'{str(Y)}-{pad_zero(M)}-{pad_zero(D)}'
    HmS=f'{pad_zero(H)}:{pad_zero(m)}:{pad_zero(S)}'
    row1=f'@{ip}'
    row2=f'{YMD} {week[W]}'
    row3=HmS    
    oled.fill(0)
    oled.text(row1, 0, 0, 1)
    oled.text(row2, 0, 8, 1)
    oled.text(row3, 0, 16, 1)
    oled.show()
    time.sleep(1)
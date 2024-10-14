import config  
import xtools   
import urequests  
import ujson
from machine import I2C, Pin
import ssd1306   
import big_symbol
import time

def get_weather(country, city, api_key):
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&lang=zh_tw&appid={api_key}'
    try:
        res=urequests.get(url)
        data=ujson.loads(res.text)
        if data['cod']==200:    # 注意是數值
            ret={'geocode': data['id'],
                 'icon': data['weather'][0]['icon'],
                 'temperature': data['main']['temp'],
                 'pressure': data['main']['pressure'],
                 'humidity': data['main']['humidity']}
            return ret
        else:
            return None
    except Exception as e:
        return None

ip=xtools.connect_wifi(config.SSID, config.PASSWORD)
if ip:
    # 設定氣象爬蟲參數
    weather_api_key=config.WEATHER_API_KEY
    city='Kaohsiung'   
    country='TW'
    # 建立 I2C 與 SSD1306_I2C 物件
    i2c=I2C(0, scl=Pin(22), sda=Pin(21)) # ESP32 I2C
    oled=ssd1306.SSD1306_I2C(128, 64, i2c)
    sb=big_symbol.Symbol(oled)
    while True:  # 每分鐘抓一次更新 OLED 顯示器
        data=get_weather(country, city, weather_api_key)
        sb.clear()
        sb.temp(0, 0)       
        sb.text(f"{data['temperature']}c", 32, 0)
        sb.humid(0, 16) 
        sb.text(f"{data['humidity']}%", 32, 16)
        sb.press(0, 32)
        sb.text(f"{data['pressure']}hPa", 32, 32)
        oled.text(xtools.tw_now(), 0, 48, 1)
        oled.text(city, 0, 56, 1)
        oled.show()
        time.sleep(60)
else:
    print('無法連線 WiFi')
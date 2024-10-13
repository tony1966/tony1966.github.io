from machine import I2C, Pin
import ssd1306
import big_symbol

i2c=I2C(0, scl=Pin(22), sda=Pin(21)) # ESP32
oled=ssd1306.SSD1306_I2C(128, 64, i2c)
sb=big_symbol.Symbol(oled)
sb.clear()
sb.temp(0, 0)
sb.text('27.85c', 32, 0)
sb.humid(0, 16)
sb.text('89.66%', 32, 16)
sb.press(0, 32)
sb.text('1021hPa', 32, 32)
oled.show()

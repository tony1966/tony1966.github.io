import ESP8266WebServer
import xtools
import config
from machine import Pin 
         
def handleRoot(socket, args):
    with open('./www5/index.html', 'r', encoding='utf-8') as f:
        html=f.read()
    ESP8266WebServer.ok(socket, "200", "text/html", html)

def handleOn(socket, args): 
    led.value(0)   # GPIO2 板載 LED 輸出 low 為亮
    ESP8266WebServer.ok(socket, "200", "text/html", "點亮")

def handleOff(socket, args): 
    led.value(1)   # GPIO2 板載 LED 輸出 high 為滅
    ESP8266WebServer.ok(socket, "200", "text/html", "熄滅")

ip=xtools.connect_wifi_led(config.SSID, config.PASSWORD) 
led=Pin(2, Pin.OUT)
led.value(1)
ESP8266WebServer.setDocPath("/www5")
ESP8266WebServer.begin(80)   
ESP8266WebServer.onPath("/", handleRoot) 
ESP8266WebServer.onPath("/on", handleOn) 
ESP8266WebServer.onPath("/off", handleOff) 

while True:
    ESP8266WebServer.handleClient()
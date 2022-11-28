import ESP8266WebServer
import xtools
import config
from machine import Pin 

ip=xtools.connect_wifi_led(config.SSID, config.PASSWORD) 
led=Pin(2, Pin.OUT)
led.value(0)
ESP8266WebServer.begin(80)              
ESP8266WebServer.setDocPath("/www4")

def handleRoot(socket, args): 
    print(args)
    with open('./www4/index.p.html', 'r', encoding='utf-8') as f:
        html=f.read()
    state='º¶·À' 
    if 'led' in args:
        if args['led']='on':
            state='ÂI«G'
            led.value(1)
        elif args['led']='off':
            state='º¶·À'
            led.value(0)
    response=html.format(state)
    ESP8266WebServer.ok(socket, "200", "text/html", response)

ESP8266WebServer.onPath("/", handleRoot) 
data={"state": "º¶·À"}
ESP8266WebServer.setTplData(data)

while True:
    ESP8266WebServer.handleClient()
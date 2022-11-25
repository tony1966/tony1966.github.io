import ESP8266WebServer
import xtools
import config

ip=xtools.connect_wifi_led(config.SSID, config.PASSWORD) 

ESP8266WebServer.begin(80)              

def handleRoot(socket, args): 
    with open('./www3/index.html', 'r', encoding='utf-8') as f:
        html=f.read()
        print(html)
    ESP8266WebServer.ok(socket, "200", "text/html", html)
def handlePage1(socket, args): 
    with open('./www3/page1.html', 'r', encoding='utf-8') as f:
        html=f.read()
        print(html)
    ESP8266WebServer.ok(socket, "200", "text/html", html) 
def handlePage2(socket, args): 
    with open('./www3/page2.html', 'r', encoding='utf-8') as f:
        html=f.read()
        print(html)
    ESP8266WebServer.ok(socket, "200", "text/html", html)

ESP8266WebServer.onPath("/", handleRoot) 
ESP8266WebServer.onPath("/page1", handlePage1) 
ESP8266WebServer.onPath("/page2", handlePage2) 

while True:
    ESP8266WebServer.handleClient()
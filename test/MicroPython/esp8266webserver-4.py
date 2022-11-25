import ESP8266WebServer
import xtools
import config

ip=xtools.connect_wifi_led(config.SSID, config.PASSWORD) 

ESP8266WebServer.begin(80)              
ESP8266WebServer.setDocPath("/www2") 

while True:
    ESP8266WebServer.handleClient()
import ESP8266WebServer
import xtools
import config

ip=xtools.connect_wifi_led(config.SSID, config.PASSWORD) 

html="""
<html>
<head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body>
   <h1>Hello World!</h1>
</body>
</html>"""

def handleRoot(socket, args):    
    global html
    ESP8266WebServer.ok(socket, "200", "text/html", html)
    
ESP8266WebServer.begin(80)
ESP8266WebServer.onPath("/", handleRoot)
while True:
    ESP8266WebServer.handleClient()
import xtools    
import config   

ip=xtools.connect_wifi_led(config.SSID, config.PASSWORD)
mac=xtools.get_id().decode("utf-8")
print("ip : ", ip)
print("mac : ", mac)
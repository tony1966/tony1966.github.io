# xtools.py for ESP8266
from machine import Pin, RTC, unique_id
import urandom, math
import time, network, urequests
import ubinascii
import config
import ntptime
import ujson

def get_id():
    return ubinascii.hexlify(unique_id()).decode('utf8')

def get_mac():
    sta=network.WLAN(network.STA_IF)
    mac=sta.config('mac')
    return ubinascii.hexlify(mac, ':').decode('utf8')

def get_num(x):
    return float("".join(ele for ele in x if ele.isdigit() or ele =="."))

def random_in_range(low=0, high=1000):
    r1 = urandom.getrandbits(32)
    r2 = r1 % (high-low) + low
    return math.floor(r2)

def map_range(x, in_min, in_max, out_min, out_max):
   return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
   
def connect_wifi(ssid=config.SSID, passwd=config.PASSWORD, led=2, timeout=20):
    wifi_led=Pin(led, Pin.OUT, value=1)
    sta=network.WLAN(network.STA_IF)
    sta.active(True)
    start_time=time.time() # 記錄時間判斷是否超時
    if not sta.isconnected():
        print("Connecting to network...")
        sta.connect(ssid, passwd)
        while not sta.isconnected():
            wifi_led.value(0)
            time.sleep_ms(300)
            wifi_led.value(1)
            time.sleep_ms(300)
            # 判斷是否超過timeout秒數
            if time.time()-start_time > timeout:
                print("Wifi connecting timeout!")
                break
    if sta.isconnected():
        for i in range(25):   # 連線成功 : 快閃 5 秒
            wifi_led.value(0)
            time.sleep_ms(100)
            wifi_led.value(1)
            time.sleep_ms(100)
        print("network config:", sta.ifconfig())
        return sta.ifconfig()[0] 

def scan_ssid():
    sta=network.WLAN(network.STA_IF)
    sta.active(True)
    aps=sta.scan()
    for ap in aps:
        ssid=ap[0].decode()
        mac=ubinascii.hexlify(ap[1], ':').decode()
        rssi=str(ap[3]) + 'dBm'
        print('{:>20} {:>20} {:>10}'.format(ssid, mac, rssi))

def show_error(final_state=0):
    led = Pin(2, Pin.OUT)   # Built-in D4
    for i in range(3):
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
    led.value(final_state)    

def webhook_post(url, value):
    print("invoking webhook")
    r = urequests.post(url, data=value)
    if r is not None and r.status_code == 200:
        print("Webhook invoked")
    else:
        print("Webhook failed")
        show_error()
    return r

def webhook_get(url):
    print("invoking webhook")
    r = urequests.get(url)
    if r is not None and r.status_code == 200:
        print("Webhook invoked")
    else:
        print("Webhook failed")
        show_error()
    return r

def urlencode(params):
    # 將字典的鍵值對轉換為 URL 編碼的字串 (k=v) 並以 & 連接多個鍵值對
    kv=['{}={}'.format(k, v) for k, v in params.items()]
    return '&'.join(kv)

def line_msg(token, message):
    url="https://notify-api.line.me/api/notify"
    headers={
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
        }     
    params={"message": message}  # 參數字典
    # 呼叫自訂的 URL 編碼函式將字典轉成 URL 字串, 再轉成 utf-8 編碼的 bytes 
    payload=urlencode(params).encode('utf-8')
    # 用編碼後的 payload 傳給 data 參數發送 POST 請求
    r=urequests.post(url, headers=headers, data=payload)  
    if r is not None and r.status_code == 200:
        print("Message has been sent.")
    else:
        print("Error! Failed to send notification message.")  
    r.close()  # 關閉連線

def tw_now():
    try: # 從 NTP 取得 UTC 時戳加 8 為台灣時間, 若成功設定 RTC
        print('Querying NTP server and set RTC time ... ', end='')
        utc=ntptime.time() # 取得 UTC 時戳
        print('OK.')
        t=time.localtime(utc + 28800) # 傳回台灣時間的元組
        rtc=RTC() # RTC 物件
        rtc.datetime(t[0:3] + (0,) + t[3:6] + (0,)) # 設定 RTC
    except:  # 查詢 NTP 失敗不設定 RTC 
        print('Failed.')
    return strftime()  # 傳回目前之日期時間字串 YYYY-mm-dd HH:MM:SS 

def strptime(dt_str, format_str="%Y-%m-%d %H:%M:%S"):
    if format_str=="%Y-%m-%d %H:%M:%S":
        year=int(dt_str[0:4])
        month=int(dt_str[5:7])
        day=int(dt_str[8:10])
        hour=int(dt_str[11:13])
        minute=int(dt_str[14:16])
        second=int(dt_str[17:19])
        return (year, month, day, hour, minute, second, 0, 0, 0)
    else:
        raise ValueError("Unsupported format string")
    
def strftime(dt=None, format_str="%Y-%m-%d %H:%M:%S"):
    if dt is None:
        dt=time.localtime()
    return format_str.replace("%Y", str(dt[0])) \
                     .replace("%m", "{:02d}".format(dt[1])) \
                     .replace("%d", "{:02d}".format(dt[2])) \
                     .replace("%H", "{:02d}".format(dt[3])) \
                     .replace("%M", "{:02d}".format(dt[4])) \
                     .replace("%S", "{:02d}".format(dt[5]))

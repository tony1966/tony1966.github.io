# esptools.py for ESP8266, 2025-04-24 updated (adapted from xtools.py)
from machine import Pin, RTC, unique_id
import urandom, time, network, urequests, ubinascii
import ntptime, ujson
import uos

def get_id():
    return ubinascii.hexlify(unique_id()).decode('utf8')

def get_mac():
    sta=network.WLAN(network.STA_IF)
    mac=sta.config('mac')
    return ubinascii.hexlify(mac, ':').decode('utf8')

def get_num(x):
    return float(''.join(filter(lambda c: c.isdigit() or c == ".", x)))

def random_in_range(low=0, high=1000):
    return urandom.getrandbits(32) % (high - low) + low

def map_range(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
   
def connect_wifi(ssid, password, led=2, timeout=20):
    wifi_led=Pin(led, Pin.OUT, value=1)
    sta=network.WLAN(network.STA_IF)
    if not sta.active():
        sta.active(True)   # 確保已啟動 WiFi
    start_time=time.time() # 記錄時間判斷是否超時
    if not sta.isconnected():
        print("Connecting to network...")
        sta.connect(ssid, password)
        while not sta.isconnected() and time.time() - start_time <= timeout:
            wifi_led.value(0)
            time.sleep_ms(300)
            wifi_led.value(1)
            time.sleep_ms(300)
        if not sta.isconnected():
            print("Wifi connecting timeout!")
            return None
    if sta.isconnected():
        for _ in range(25):  # 連線成功 : 快閃 5 秒
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
        print(f'{ssid} {mac} {rssi}')

def show_error(led=2, final_state=0):
    led=Pin(led, Pin.OUT)   # D1 mini built-in D4=LED 2
    for i in range(3):
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
    led.value(final_state)    

def webhook_post(url, value, led=2):
    try:
        r=urequests.post(url, data=value)
        if r.status_code == 200:
            print("Webhook invoked")
        else:
            print("Webhook failed")
            show_error(led)
    finally:
        r.close()  # 釋放資源
    return r

def webhook_get(url, led=2):
    try:
        r=urequests.get(url)
        if r.status_code == 200:
            print("Webhook invoked")
        else:
            print("Webhook failed")
            show_error(led)
    finally:
        r.close()  # 釋放資源
    return r

def urlencode(params):
    # 將字典的鍵值對轉換為 URL 編碼的字串 (k=v) 並以 & 連接多個鍵值對
    kv=['{}={}'.format(k, v) for k, v in params.items()]
    return '&'.join(kv)

def tw_now():
    try: # 從 NTP 取得 UTC 時戳加 8 為台灣時間, 若成功設定 RTC
        print('Querying NTP server and set RTC time ... ', end='')
        utc=ntptime.time() # 取得 UTC 時戳
        print('OK.')
        t=time.localtime(utc + 28800) # 傳回台灣時間的元組
        RTC().datetime(t[0:3] + (0,) + t[3:6] + (0,))
    except Exception as e:  # 加入例外處理
        print(f'Failed. {e}')
    return strftime()  # 傳回目前之日期時間字串 YYYY-mm-dd HH:MM:SS 

def strptime(dt_str):
    t=time.mktime((
        int(dt_str[0:4]), int(dt_str[5:7]), int(dt_str[8:10]),
        int(dt_str[11:13]), int(dt_str[14:16]), int(dt_str[17:19]),
        0, 0))
    return time.localtime(t)
    
def strftime(dt=None, format_str="%Y-%m-%d %H:%M:%S"):
    if dt is None:
        dt=time.localtime()
    return format_str.replace("%Y", str(dt[0])) \
                     .replace("%m", "{:02d}".format(dt[1])) \
                     .replace("%d", "{:02d}".format(dt[2])) \
                     .replace("%H", "{:02d}".format(dt[3])) \
                     .replace("%M", "{:02d}".format(dt[4])) \
                     .replace("%S", "{:02d}".format(dt[5]))


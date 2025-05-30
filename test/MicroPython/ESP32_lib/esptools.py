# esptools.py for ESP32, 2025-04-21 updated (adapted from xtools.py)
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

def get_headers(service, token=None, api_key=None):
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
        } # 須有初始值 
    if service == 'telegram' and token: # 根據服務類型返回標頭
        headers["Authorization"]="Bearer " + token
    elif service == 'openai' and api_key:
        headers["Authorization"]="Bearer " + api_key
        headers["Content-Type"]="application/json"
    return headers

def telegram_text(token, chat_id, text):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    headers=get_headers('telegram', token=token)
    params={'chat_id': chat_id, 'text': text}  # 參數字典
    # 將參數字典轉成 URL 字串, 再轉成 utf-8 編碼的 bytes 
    data=urlencode(params).encode('utf-8')
    # 用編碼後的 payload 傳給 data 參數發送 POST 請求
    r=None
    try:  # 發送 POST 請求
        r=urequests.post(url, headers=headers, data=data)
        # 判斷是否成功
        if r.status_code == 200:
            print('The message has been sent.')
            return True
        else:
            print('Error! Failed to send the message.')
            return False
    except Exception as e:
        print(f'Exception occurred : {e}')
        return False
    finally:
        if r:
            r.close()    

def telegram_photo_url(token, chat_id, photo_url, caption=None):
    # 透過 Telegram 發送網路圖片
    url=f'https://api.telegram.org/bot{token}/sendPhoto'
    headers=get_headers('telegram', token=token)
    # 構造請求的數據，包含圖片的 URL
    if caption:
        params={
            'chat_id': chat_id,
            'photo': photo_url,
            'caption': caption,
            'parse_mode': 'Markdown'
            }
    else:
        params={'chat_id': chat_id, 'photo': photo_url}
    # 轉成 URL 字串並用 utf-8 編碼為 bytes 
    data=urlencode(params).encode('utf-8')
    r=None
    try:  # 發送 POST 請求
        r=urequests.post(url, headers=headers, data=data)
        # 判斷是否成功
        if r.status_code == 200:
            print('The image has been sent.')
            return True
        else:
            print('Error! Failed to send the image.')
            return False
    except Exception as e:
        print(f'Exception occurred : {e}')
        return False
    finally:
        if r:
            r.close()    

def telegram_photo_file(token, chat_id, photo_path, caption=None):
    url=f'https://api.telegram.org/bot{token}/sendPhoto'
    boundary='----WebKitFormBoundary7MA4YWxkTrZu0gW'
    try:
        with open(photo_path, 'rb') as f:   # 讀取圖片
            photo_data=f.read()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return False
    # 建構 multipart body
    payload=[]
    payload.append('--' + boundary)
    payload.append(f'Content-Disposition: form-data; name="chat_id"\r\n')
    payload.append(str(chat_id))
    if caption:
        payload.append('--' + boundary)
        payload.append(f'Content-Disposition: form-data; name="caption"\r\n')
        payload.append(caption)
    payload.append('--' + boundary)
    payload.append(f'Content-Disposition: form-data; name="photo"; filename="{photo_path}"')
    payload.append('Content-Type: image/jpeg\r\n')
    # 組裝 payload
    body=b''  
    for part in payload:
        if isinstance(part, str):
            body += part.encode('utf-8') + b'\r\n'
        else:
            body += part + b'\r\n'
    body += photo_data + b'\r\n'
    body += ('--' + boundary + '--\r\n').encode('utf-8')
    headers={
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'Content-Length': str(len(body))
        }
    r=None
    try:
        r=urequests.post(url, data=body, headers=headers)
        print("Status:", r.status_code)
        print("Response:", r.text)
        r.close()
        return True
    except Exception as e:
        print("Request error:", e)
        return False
    finally:
        if r:
            r.close()    

def ask_gpt(prompt, api_key, model='gpt-3.5-turbo'):
    url='https://api.openai.com/v1/chat/completions'
    headers=get_headers('openai', api_key=api_key)
    # 建立 data 參數字典
    data={
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}]
        }
    # 將字典轉成字串後再編碼成 UTF-8
    payload=ujson.dumps(data).encode('utf-8')
    # 發送 POST 請求
    response=urequests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        reply=response.json() # 轉成字典
        return reply['choices'][0]['message']['content']
    else:
        return response.json()  # 返回錯誤信息

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

def set_ap(led=2):
    html='''
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
      </head>
      <body>
        %s
      </body>
    </html>
    '''
    form='''
        <form method='get' action='/update_ap' 
        style='width: max-content; margin: 10px auto'>
          <h2 style='text-align: center; font-size: 20px'>設定 WiFi 基地台</h2>
          <div style='display: block; margin-bottom: 20px'>
            <label for='ssid' style='display: block; font-size: 16px'>SSID</label>
            <input type='text' id='ssid' name='ssid' 
            style='padding: 10px 8px; width: 100%; font-size: 16px'>
          </div>
          <div style='display: block; margin-bottom: 20px'>
            <label for='pwd' style='display: block; font-size: 16px'>Password</label>
            <input type='text' id='pwd' name='pwd' 
            style='padding: 10px 8px; width: 100%; font-size: 16px'>
          </div>
          <button type="submit" style='width:100%;font-size: 16px'>連線</button>
        </form>
    '''
    ok='''
       <h2>WiFi 連線成功<br>IP : <a href={0}>{0}</a></h2>
       <a href=192.168.4.1>
         <button style="width:100%;font-size: 16px">重新設定</button>
       </a>              
    '''
    ng='''
       <h2 style="text-align: center;">WiFi 基地台連線失敗<br> 
       按 Reset 鈕後重新設定</h2>
       <a href="192.168.4.1">
         <button style="width:100%;font-size: 16px">重新設定</button>
       </a>   
    '''
    wifi_led=Pin(led, Pin.OUT, value=1)  # 預設熄滅板上 LED
    ap=network.WLAN(network.AP_IF)       # 開啟 AP 模式
    ap.active(True)
    sta=network.WLAN(network.STA_IF)     # 開啟 STA 模式
    sta.active(True)
    import socket
    addr=socket.getaddrinfo('192.168.4.1', 80)[0][-1] # 傳回 (ip, port)
    s=socket.socket()  # 建立伺服端 TCP socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 網址可重複請求
    s.bind(addr)  # 綁定 192.168.4.1 的 80 埠
    s.listen(5)   # 最多同時 5 個連線
    print('網頁伺服器正在監聽 : ', addr)
    while True:   # 監聽 192.168.4.1 的 80 埠
        cs, addr=s.accept()  
        print('發現來自客戶端的連線 : ', addr)
        data=cs.recv(1024)      
        request=str(data, 'utf8')   
        print(request, end='\n')
        del data, addr
        if request.find('update_ap?') == 5:  # 檢查是否為更新之 URL 
            # 擷取請求參數中的 SSID 與密碼
            para=request[request.find('ssid='):request.find(' HTTP/')]
            ssid=para.split('&')[0].split('=')[1] 
            pwd=para.split('&')[1].split('=')[1]
            sta.connect(ssid, pwd)       # 連線 WiFi 基地台
            start_time=time.time()       # 紀錄起始時間  
            while not sta.isconnected(): # 連線 WiFi (15 秒)
                wifi_led.value(0)  # 讓板載 LED 閃爍
                time.sleep_ms(300)
                wifi_led.value(1)
                time.sleep_ms(300)                
                if time.time()-start_time > 15: # 是否超過連線秒數
                    print('WiFi 連線逾時!')
                    break  # 逾時跳出無限迴圈
            # 確認是否連線成功
            if sta.isconnected():     # WiFi 連線成功
                print('WiFi 連線成功 : ', sta.ifconfig())
                ip=sta.ifconfig()[0]  # 取得 ip
                print('取得 IP : ' + ip)
                with open('config.py', 'w', encoding='utf-8') as f:
                    f.write(f'SSID="{ssid}"\nPASSWORD="{pwd}"') # 更新設定檔
                cs.send(html % ok.format(ip))  # 回應連線成功頁面
                for i in range(25):   # 連線成功 : 快閃 5 秒
                    wifi_led.value(0)
                    time.sleep_ms(100)
                    wifi_led.value(1)
                    time.sleep_ms(100)
                cs.close()
                s.close()
                return ip
            else:
                print('WiFi 連線失敗 : 請按 Reset 鈕後重設.')
                wifi_led.value(1)     # 連線失敗 : 熄滅 LED
                cs.send(html % ng)    # 回應連線失敗頁面
                cs.close()
                s.close()
                return None
        else:  # 顯示設定 WiFi 頁面
            cs.send(html % form)  # 回應設定 WiFi 頁面
        cs.close()
        del cs, request

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


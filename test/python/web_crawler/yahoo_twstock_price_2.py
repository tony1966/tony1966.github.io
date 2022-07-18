import re
import time
import random
import requests
from bs4 import BeautifulSoup

def yahoo_twstock_crawler(stock):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/102.0.0.0 Safari/537.36'}
    url=f'https://tw.stock.yahoo.com/quote/{stock}' 
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text, 'lxml')
    # 擷取股價
    tag=soup.select('span[class*="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)"]')
    price=float(tag[0].text)
    # 擷取漲跌價
    tag=soup.select('span[class*="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c)"]')
    if 'C($c-trend-up)' in tag[0].attrs['class']:   
        change_price='+' + tag[0].text    
    elif 'C($c-trend-down)' in tag[0].attrs['class']:   
        change_price='-' + tag[0].text   
    else:    
        change_price=tag[0].text
    # 擷取漲跌幅
    tag=soup.select('span[class*="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c)"]')
    change_quote=tag[0].text[1:-1]
    if 'C($c-trend-up)' in tag[0].attrs['class']:   
        change_quote=f'(+{change_quote})'   
    elif 'C($c-trend-down)' in tag[0].attrs['class']:   
        change_quote=f'(-{change_quote})'   
    else:   
        change_quote=f'({change_quote})'
    # 擷取趨勢摘要
    tag=soup.select('span[class*="Fz(16px) Mb(4px)"]')
    if tag:
        trend_note=tag[0].text.split()[0]
    else:
        trend_note=''
    return price, change_price, change_quote, trend_note

def notify(msg, token):
    url="https://notify-api.line.me/api/notify"
    headers={"Authorization": "Bearer " + token}
    payload={"message": msg}
    r=requests.post(url, headers=headers, params=payload)
    return "訊息發送成功！"

stocks=['0050', '0056', '2330', '2303', '2412', '00894']
alert_msg_list=['\n注意! 盤中漲跌幅超過 2% :']
for stock in stocks:
    price, change_price, change_quote, trend_note=yahoo_twstock_crawler(stock)
    alert_msg=f'{stock} {price} {change_price} {change_quote} {trend_note}'
    print(alert_msg)
    change_quote2=float(re.search(r'\d+\.\d+', change_quote).group())
    if change_quote2 > 2 or change_quote2 < -2:
        alert_msg_list.append(alert_msg)
    time.sleep(random.randint(1, 5))
print(alert_msg_list)
if len(alert_msg_list) > 1:
    msg='\n'.join(alert_msg_list)
    token='ud7PaDL45fz849A0e1f5oaMCbRIkxMXapQCt7PfNkzz'
    notify(msg, token)
   
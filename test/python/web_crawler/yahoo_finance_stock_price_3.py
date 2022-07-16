import re
import time
import random
import requests
from bs4 import BeautifulSoup

def yahoo_stock_crawler(stock):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/102.0.0.0 Safari/537.36'}
    url=f'https://finance.yahoo.com/quote/{stock}?p={stock}'
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text, 'lxml')
    price=soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    changes=soup.findAll('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'})
    change_price=changes[0].find('span').text
    change_quote=changes[1].find('span').text
    return float(price.text), change_price, change_quote

def notify(msg, token):
    url="https://notify-api.line.me/api/notify"
    headers={"Authorization": "Bearer " + token}
    payload={"message": msg}
    r=requests.post(url, headers=headers, params=payload)
    return "訊息發送成功！"

stocks=['0050', '0056', '2330', '2303', '2412', '00894']
alert_msg_list=['\n注意! 盤中漲跌幅超過 2% :']
for stock in stocks:
    id=stock + '.TW'
    price, change_price, change_quote=yahoo_stock_crawler(id)
    alert_msg=f'{stock} {price} {change_price} {change_quote}'
    print(alert_msg)
    change_quote2=float(re.search("\d+\.\d+", change_quote).group())
    if change_quote2 > 2 or change_quote2 < -2:
        alert_msg_list.append(alert_msg)
    time.sleep(random.randint(1, 5))
print(alert_msg_list)
if len(alert_msg_list) > 1:
    msg='\n'.join(alert_msg_list)
    token='ud7PaDL45fz849A0e1f5oaMCbRIkxMXapQCt7PfNkzz'
    notify(msg, token)
   
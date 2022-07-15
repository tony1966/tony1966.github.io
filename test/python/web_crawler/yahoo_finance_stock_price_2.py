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

price, change_price, change_quote=yahoo_stock_crawler('2330.TW')
print(f'{price} {change_price} {change_quote}')

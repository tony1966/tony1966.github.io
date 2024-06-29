import requests   
from bs4 import BeautifulSoup
import re
import csv
import time

url=f'https://books.toscrape.com/'
res=requests.get(url)    
soup=BeautifulSoup(res.text, 'lxml')
page_li=soup.select_one('.current')
pages=int(page_li.text.strip().split('of')[1])
csv_file='books.toscrape.com.csv'
with open(csv_file, 'w+', newline='', encoding='utf-8') as f:
    writer=csv.writer(f)
    for i in range(pages):
        print(f'擷取第 {i + 1} 頁 ... ', end='')
        url=f'https://books.toscrape.com/catalogue/page-{i+1}.html'    
        res=requests.get(url)    
        soup=BeautifulSoup(res.text, 'lxml')
        links=soup.select('article > h3 > a')
        prices=soup.select('article > div.product_price > p.price_color')
        book_names=[link.get('title') for link in links]
        reg=r'\d+\.\d+'
        book_prices=[float(re.findall(reg, price.text)[0]) for price in prices]
        zipped=zip(book_names, book_prices)
        data=[(z[0], z[1]) for z in zipped]
        writer.writerows(data)
        print(f'存檔完成!')
    time.sleep(0.5)
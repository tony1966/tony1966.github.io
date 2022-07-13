import requests
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def coingecko_btc_crawler(url):
    res=requests.get(url)
    prices=res.json()['stats']
    df=pd.DataFrame(prices)
    df.columns=['datetime', 'TWD']
    df['datetime']=pd.to_datetime(df['datetime'], unit='ms')
    df.index=df['datetime']
    return df

def notify_image(msg, token, image):
    url='https://notify-api.line.me/api/notify'
    headers={'Authorization': 'Bearer ' + token}
    data={'message': msg}
    image=open(image, 'rb')
    imageFile={'imageFile': image}
    r=requests.post(url, headers=headers, data=data, files=imageFile)
    if r.status_code==requests.codes.ok:
        return '圖片發送成功！'
    else:
        return f'圖片發送失敗: {r.status_code}'

url='https://www.coingecko.com/price_charts/1/twd/90_days.json'
btc=coingecko_btc_crawler(url)
btc['100MA']=btc['TWD'].rolling(window=100).mean()
btc[['TWD', '100MA']].plot(kind='line')
last_time=str(btc.iloc[-1:].index.values[0])[0:19]
last_price=int(btc.iloc[-1:]["TWD"].values[0])
plt.title(f'Bit Coin {last_time} NT${last_price}')
plt.xlabel('')
plt.ylabel('Price(TWD)')
plt.grid(True)
plt.savefig('btc_prices.jpg')
img=Image.open('btc_prices.jpg')  
img=img.crop((18, 26, 590, 453))
img.save('btc_prices.jpg')
token='ud7PaDL45fz849A0e1f5oaMCbRIkxMXapQCt7PfNkzz'
msg='Bit Coin'
notify_image(msg, token, 'btc_prices.jpg')
plt.show()
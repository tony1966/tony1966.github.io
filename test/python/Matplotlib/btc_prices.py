import requests
import pandas as pd
import matplotlib.pyplot as plt

def coingecko_btc_crawler(url):
    res=requests.get(url)
    prices=res.json()['stats']
    df=pd.DataFrame(prices)
    df.columns=['datetime', 'TWD']
    df['datetime']=pd.to_datetime(df['datetime'], unit='ms')
    df.index=df['datetime']
    return df

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
plt.show()
import yfinance as yf
from FinMind.data import DataLoader
import pandas as pd
import mplfinance as mpf

def get_yf(symbol, start, end, interval='1d'):
    df=yf.download(symbol, start=start, end=end, interval=interval)
    df.columns=[column.lower() for column in df.columns]
    df.open=[round(i, 2) for i in df.open]
    df.high=[round(i, 2) for i in df.high]
    df.low=[round(i, 2) for i in df.low]
    df.close=[round(i, 2) for i in df.close]
    return df

def get_fm(symbol, start, end, token):
    data_loader=DataLoader()
    data_loader.login_by_token(api_token=token)
    df=data_loader.taiwan_stock_daily(stock_id=symbol, start_date=start, end_date=end)
    df['date']=pd.to_datetime(df['date'])
    df=df.set_index(df['date'])
    columns={'open': 'Open', 'max': 'High', 'min': 'Low', 'close': 'Close', 'Trading_Volume': 'Volume'}
    df=df.rename(columns=columns)
    return df

class KBar():
    def __init__(self, df):
        self.df=df
        self.addplots=[]
    def addplot(self, data, **kwargs):
        plot=mpf.make_addplot(data, **kwargs)
        self.addplots.append(plot)
    def plot(self, **kwargs):
        color=mpf.make_marketcolors(up='red', down='green', inherit=True)   
        font={'font.family': 'Microsoft JhengHei'}   
        style=mpf.make_mpf_style(base_mpf_style='default',
                                 marketcolors=color,
                                 rc=font)
        kwargs['type']='candle'
        kwargs['style']=style
        kwargs['addplot']=self.addplots
        mpf.plot(self.df, **kwargs)

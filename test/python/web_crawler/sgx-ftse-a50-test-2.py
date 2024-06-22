import requests 
import csv

url='https://api.sgx.com/derivatives/v1.0/contract-code/' +\
    'CN?order=asc&orderby=delivery-month&category=futures'    
res=requests.get(url)
data=res.json()
csv_file='sgx-ftse-a50-2.csv'
with open(csv_file, 'w+', newline='', encoding='utf-8') as f:      
    writer=csv.writer(f)
    header=['最近更新時間',
            '最近到期日',
            '代號',
            '盤別',
            '漲跌',
            '漲跌幅',
            '開盤價',
            '最高價',
            '最低價',
            '收盤價',
            '結算價',
            '成交量',
            '未平倉量']
    writer.writerow(header)
    for item in data['data']:
        row=[]
        row.append(item['last-update-time'])
        row.append(item['last-trading-date'])
        row.append(item['symbol'])
        if item['current-trading-session']=='0':
            row.append('T')
        else:
            row.append('T+')
        row.append(item['change-abs'])
        row.append(item['change-percentage'])
        row.append(item['session-open-abs'])
        row.append(item['session-traded-high-abs'])
        row.append(item['session-traded-low-abs'])
        row.append(item['last-traded-price-abs'])
        row.append(item['daily-settlement-price-abs'])
        row.append(item['total-volume'])
        row.append(item['open-interest'])
        writer.writerow(row)
    print(f'擷取結果儲存於 ./{csv_file} 檔案')
    
import requests 
import json

url='https://api.sgx.com/derivatives/v1.0/contract-code/' +\
    'CN?order=asc&orderby=delivery-month&category=futures'    
res=requests.get(url)
#data=json.loads(res.text)
data=res.json()
with open('sgx-ftse-a50.json', 'w', encoding='utf-8') as f:      
    json.dump(data, f)
print('擷取結果儲存於 ./sgx-ftse-a50.json 檔案')
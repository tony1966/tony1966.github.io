import requests   
from bs4 import BeautifulSoup  

def line_notify(msg, token):
    url="https://notify-api.line.me/api/notify"
    headers={"Authorization": "Bearer " + token,
             "Content-Type": "application/x-www-form-urlencoded"
             }
    payload={"message": msg}
    r=requests.post(url, headers=headers, params=payload)
    return r.status_code

def get_today_66():
    url='https://activity.books.com.tw/crosscat/ajaxinfo/' +\
        'getBooks66OfTheDayAjax/P?uniqueID=E180629000000001_94'
    try:
        res=requests.get(url)
        soup=BeautifulSoup(res.text, 'lxml') 
        book_url=soup.find('a').get('href', None)
        book_name=soup.find('img').get('alt', None)
        book_img=soup.find('img').get('src', None)
        book_price=soup.select_one('ul.price').get_text()
        book_price=book_price.replace('\n', '').replace('66', ' 66')
        msg=f'\n❖ {book_name}\n{book_price}\n▶ {book_url}'
        return msg 
    except Exception as e: 
        return None

if __name__ == '__main__':
    token='lKrAsAlXZDY5I4nrdEr86fTFSIC2ershE6o9bI5ciye'
    msg=get_today_66()
    if msg:  
        code=line_notify(msg, token)
        if code==200:
            print('Line 訊息發送成功!')
        else:
            print(f'Line 訊息發送失敗! (code={code})')
    else:
        print('無資料')
    

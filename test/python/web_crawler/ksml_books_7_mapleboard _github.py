from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import re
from datetime import datetime
import time
import requests

def line_notify(msg, token):
    url="https://notify-api.line.me/api/notify"
    headers={"Authorization": "Bearer " + token,
             "Content-Type": "application/x-www-form-urlencoded"
             }
    payload={"message": msg}
    r=requests.post(url, headers=headers, params=payload)
    return r.status_code

def get_books(account, password):
    try:
        # 登入我的書房
        options=Options()
        options.add_argument("--headless")
        driverpath='/usr/lib/chromium-browser/chromedriver'
        service=Service(driverpath)
        browser=webdriver.Chrome(options=options, service=service)
        browser.implicitly_wait(20)
        browser.get("https://webpacx.ksml.edu.tw/personal/")
        loginid=browser.find_element(By.ID, "loginid")
        loginid.send_keys(account)
        pincode=browser.find_element(By.ID, 'pincode')
        pincode.send_keys(password)
        div_btn_grp=browser.find_element(By.CLASS_NAME, 'btn_grp')
        login_btn=div_btn_grp.find_element(By.TAG_NAME, 'input')
        login_btn.click()
        # 擷取借閱紀錄
        div_redblock=browser.find_element(By.CLASS_NAME, 'redblock')
        div_redblock.click()
        books=browser.find_elements(By.CLASS_NAME, 'bookdata')
        borrow_books=[]
        for book in books:
            item=dict()
            book_name=book.find_element(By.XPATH, './h2/a').text    
            item['book_name']=book_name.replace('/', '').strip()
            reg=r'\d{4}-\d{2}-\d{2}'
            due_date=book.find_element(By.XPATH, './ul[4]/li[2]').text
            item['due_date']=re.findall(reg, due_date)[0] 
            due_times=book.find_element(By.XPATH, './ul[5]/li[1]').text
            item['due_times']=re.findall(r'\d{1}', due_times)[0]   
            borrow_books.append(item)
        browser.back() # 回上一頁
        # 擷取預約紀錄
        div_blueblock=browser.find_element(By.CLASS_NAME, 'blueblock')
        browser.implicitly_wait(20)
        div_blueblock.click()
        books=browser.find_elements(By.CLASS_NAME, 'bookdata')
        reserve_books=[]
        for book in books:
            item=dict()
            book_name=book.find_element(By.XPATH, './h2/a').text    
            item['book_name']=book_name.replace('/', '').strip()
            sequence=book.find_element(By.XPATH, './ul[7]/li[1]').text
            if '預約待取' in sequence:  # 已到館
                item['ready_for_pickup']=True
                reg=r'\d{4}-\d{2}-\d{2}'
                item['expiration']=re.findall(reg, sequence)[0]
                item['sequence']='0'
            else: # 預約中
                item['ready_for_pickup']=False
                item['expiration']=''
                item['sequence']=re.findall(r'\d+', sequence)[0]
            reserve_books.append(item)
        browser.close()
        return (borrow_books, reserve_books)        
    except Exception as e:
        print(e)
        return None, None
    
if __name__ == '__main__':
    start=time.time()
    token='7CLpVmFpNihuN6GB0bQcc5M1nOhpAtony1966QFMgzz'   # 範例權仗
    users=[['family87', '123456'],
           ['amy08123', '123456'],
           ['kelly19', '123456'],
           ['peter120', '123456'],
           ['shinping92', '123456'],
           ['daddy587', '123456']]      # 範例帳號  
    for user in users:
        account=user[0]
        password=user[1]
        borrow_books, reserve_books=get_books(account, password)
        if borrow_books: 
            borrow=[]
            for book in borrow_books:
                book_name=book['book_name']   
                due_times=book['due_times']
                due_date=book['due_date']
                due_date=datetime.strptime(due_date, '%Y-%m-%d')   
                today_str=datetime.today().strftime('%Y-%m-%d')   
                today=datetime.strptime(today_str, "%Y-%m-%d")   
                delta=(due_date-today).days
                if delta < 0:
                    msg=f'🅧 {book_name} (逾期 {abs(delta)} 天)'
                    borrow.append(msg)
                elif delta == 0:
                    msg=f'⓿ {book_name} (今日到期, 續借次數 {due_times})'
                    borrow.append(msg)
                elif delta == 1:   
                    msg=f'❶ {book_name} (明日到期, 續借次數 {due_times})'
                    borrow.append(msg)
                elif delta == 2:   
                    msg=f'❷ {book_name} (後天到期, 續借次數 {due_times})'
                    borrow.append(msg)
                elif 2 < delta < 8:   
                    msg=f'✦ {book_name} ({book["due_date"]} 到期, '\
                        f'續借次數 {due_times})'
                    borrow.append(msg)                  
            if len(borrow) != 0:
                borrow.insert(0, f'\n❖ {account} 的借閱 :')
                msg='\n'.join(borrow)
                code=line_notify(msg, token)
                if code==200:
                    print('Line 訊息發送成功!')
                else:
                    print(f'Line 訊息發送失敗! (code={code})')
        if reserve_books:
            reserve=[]
            i=0
            j=['①', '②', '③', '④', '⑤']
            k=['❶', '❷', '❸', '❹', '❺']
            for book in reserve_books:
                book_name=book['book_name']
                sequence=book['sequence']
                ready_for_pickup=book['ready_for_pickup']
                expiration=book['expiration']
                if ready_for_pickup:
                    msg=f'{k[i]} {book_name} (已到館, 保留期限 {expiration})'
                else:
                    msg=f'{j[i]} {book_name} (順位 {sequence})'
                reserve.append(msg)
                i += 1
            if len(reserve) != 0:
                reserve.insert(0, f'\n❖ {account} 的預約 :')
                msg='\n'.join(reserve)
                code=line_notify(msg, token)
                if code==200:
                    print('Line 訊息發送成功!')
                else:
                    print(f'Line 訊息發送失敗! (code={code})')
    end=time.time()
    print(f'執行時間:{end-start}')
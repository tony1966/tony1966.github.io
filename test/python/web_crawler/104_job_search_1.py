from selenium import webdriver
import re
import time

driver=webdriver.Firefox()   
driver.implicitly_wait(20)   
url='https://www.104.com.tw/'     
driver.get(url)
keyword=driver.find_element('class name', 'form-control')
keyword.send_keys('Python')
buttons=driver.find_elements('tag name', 'button')
buttons[2].click()
for i in range(5):    
  js='window.scrollTo(0, document.body.scrollHeight)'   
  driver.execute_script(js)
  time.sleep(0.5)
articles=driver.find_elements('tag name', 'article')
print(len(articles))
for i in range(len(articles)):
    job_name=articles[i].get_attribute('data-job-name')
    cust_name=articles[i].get_attribute('data-cust-name')
    '''try:
        link=articles[i].find_element('tag name', 'a')
        url=link.get_attribute('href')
    except Exception as e:
        url='''''
    if job_name:
        print(f'工作名稱: {job_name}')
        print(f'徵求公司: {cust_name}')
        link=articles[i].find_element('tag name', 'a')
        url=link.get_attribute('href')
        print(f'詳細資訊: {url}\n')
    else:
        print(f'索引 {i} 無資料\n')
driver.close()

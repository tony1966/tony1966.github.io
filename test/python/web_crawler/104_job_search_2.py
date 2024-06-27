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
page_select=driver.find_element('class name', 'gtm-paging-top')
page_option=page_select.find_element('tag name', 'option')
pages_str=page_option.text.split('/')[1]
pages=int(re.findall(r'\d+', pages_str)[0])
print(f'總頁數: {pages}')
for i in range(pages):    
  js='window.scrollTo(0, document.body.scrollHeight)'   
  driver.execute_script(js)
  time.sleep(0.5)
articles=driver.find_elements('tag name', 'article')
print(f'總筆數: {len(articles)}')
for i in range(len(articles)):
    job_name=articles[i].get_attribute('data-job-name')
    cust_name=articles[i].get_attribute('data-cust-name')
    if job_name:
        print(f'{i}. {job_name}')
        print(f'❖ {cust_name}')
        link=articles[i].find_element('tag name', 'a')
        url=link.get_attribute('href')
        print(f'▶ {url}\n')
    else:
        print(f'索引 {i} 無資料\n')
driver.close()

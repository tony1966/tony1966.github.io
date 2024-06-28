from selenium import webdriver
import csv
import time

driver=webdriver.Firefox()   
driver.implicitly_wait(10)   
url='https://www.nba.com/stats/players/traditional'     
driver.get(url)
try:
    accept_btn=driver.find_element('id', 'onetrust-accept-btn-handler')
    accept_btn.click()
except Exception as e:
    pass
selects=driver.find_elements('class name', 'DropDown_select__4pIg9')
options=selects[25].find_elements('tag name', 'option')
pages=len(options) - 1
print(f'總頁數: {pages}')
for page in range(pages):
    print(f'擷取第 {page + 1} 頁 ...')
    table=driver.find_element('class name', 'Crom_table__p1iZz')
    trs=table.find_elements('tag name', 'tr')
    ths=trs[0].find_elements('tag name', 'th') 
    header=[th.text for th in ths if th.text != '']
    rows=[]
    rows.append(header)
    for tr in trs[1:]:
       cols=[]
       tds=tr.find_elements('tag name', 'td')
       for td in tds:
           cols.append(td.text)
       rows.append(cols)
    csv_file=f'nba_players_stata_page_{page + 1}.csv'
    with open(csv_file, 'w', newline='') as f:
      writer=csv.writer(f)
      writer.writerows(rows)
    print(f'第 {page + 1} 頁已存檔 {csv_file}')
    class_name='Pagination_button__sqGoH'
    page_buttons=driver.find_elements('class name', class_name)
    page_buttons[1].click()
    time.sleep(1)
print('NBA 球員資料已擷取存檔完成!')
driver.close()
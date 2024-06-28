from selenium import webdriver
import csv

driver=webdriver.Firefox()   
driver.implicitly_wait(20)   
url='https://www.nba.com/stats/players/traditional'     
driver.get(url)
try:
    accept_btn=driver.find_element('id', 'onetrust-accept-btn-handler')
    accept_btn.click()
except Exception as e:
    pass
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
csv_file='nba_players_stata_page_1.csv'
with open(csv_file, 'w', newline='') as f:
  writer=csv.writer(f)
  writer.writerows(rows)
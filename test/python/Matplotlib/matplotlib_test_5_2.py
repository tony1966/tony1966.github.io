import matplotlib.pyplot as plt 
week=['Sun','Mon','Tue','Wen','Thu','Fri','Sat']      #X 軸
this_week=[25.4, 23.7, 28.6, 29.2, 24.8, 22.5, 21.9]  #本周氣溫
last_week=[22.2, 25.2, 26.6, 22.8, 20.1, 24.3, 28.9]  #上周氣溫
plt.plot(week, last_week, 'b-s')                     
plt.plot(week, this_week, 'r--o')    
plt.legend(['last_week', 'this_week'], loc='lower left') #設定圖例標籤與位置
plt.title('Temperature Comparison') 
plt.xlabel('Week day')
plt.ylabel('Celsius') 
plt.show() 
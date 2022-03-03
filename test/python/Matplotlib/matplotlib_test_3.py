import matplotlib.pyplot as plt
week=['Sun','Mon','Tue','Wen','Thu','Fri','Sat']              #X 軸
this_week=[25.4, 23.7, 28.6, 29.2, 24.8, 22.5, 21.9]     #本周氣溫
last_week=[22.2, 25.2, 26.6, 22.8, 20.1, 24.3, 28.9]     #上周氣溫
plt.plot(week,this_week,'r--o',week, last_week,'b-s')    #繪製兩組資料
plt.show()
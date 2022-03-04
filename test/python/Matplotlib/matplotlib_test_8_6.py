import matplotlib.pyplot as plt
x=['2022-02-25','2022-02-26','2022-02-27','2022-02-28',
   '2022-03-01','2022-03-02','2022-03-03']              #X 軸(日期)
temp=[25.4, 23.7, 28.6, 29.2, 24.8, 22.5, 21.9]         #氣溫
humid=[56, 63, 75, 72, 66, 59, 77]                      #濕度
plt.plot(x,temp,'r--o',x, humid,'b-s')                  #繪製兩組資料
plt.title('Temperature & Humidity')                     #設定圖形標題
plt.xlabel('day')                                       #設定 X 軸標籤
plt.ylabel('Temperature & Humidity')                    #設定 Y 軸標籤
plt.xticks(x, rotation=20)
plt.show()
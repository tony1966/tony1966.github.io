import matplotlib.pyplot as plt

plt.rcParams["font.family"]=["Microsoft JhengHei"]    # 使用微軟正黑體
week=['日','一','二','三','四','五','六']
temperature=[25.4, 23.7, 28.6, 29.2, 24.8, 22.5, 21.9]
plt.plot(week, temperature)
plt.title('溫度變化圖')                      
plt.xlabel('星期')                                                 
plt.ylabel('攝氏')     
plt.text('一', 23.2, '太平洋高壓使溫度回升')
plt.text('三', 28, '冷鋒過境溫度驟降', color='blue', fontsize=10, alpha=0.5)
plt.text('三', 28, '冷鋒過境溫度驟降')
plt.show()
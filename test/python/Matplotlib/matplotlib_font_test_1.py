import matplotlib.pyplot as plt
week=['日','一','二','三','四','五','六']
temperature=[6.4, 5.7, 2.6, -1.2, -3.8, 0.5, 2.9]
plt.plot(week, temperature)
plt.title('溫度變化圖')                      
plt.xlabel('星期')                                                 
plt.ylabel('攝氏')     
plt.show()
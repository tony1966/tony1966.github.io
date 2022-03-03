import numpy as np
import matplotlib.pyplot as plt 
x=(2015, 2016, 2017, 2018, 2019)      #X 軸
y1=(4.33, 5.67, 3.78, 5.62, 6.7)      #Y軸1=0056殖利率
y2=(3.01, 1.28, 6.1, 7.1, 7.22)       #Y軸2=0050殖利率
plt.plot(x, y1, 'r--o', label='0056') #指定資料之圖例標籤
plt.plot(x, y2, 'b:d', label='0050')  #指定資料之圖例標籤
plt.legend()                          #顯示圖例
plt.title('ETF Dividend Yield')       #設定圖形標題
plt.xlabel('Year')                    #設定 X 軸標籤
plt.ylabel('Dividend yield(%)')       #設定 Y 軸標籤
plt.show()
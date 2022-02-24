import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)            #X 軸
y1=np.sin(x)                              #Y軸1=sin(x)
y2=np.cos(x)                             #Y軸2=cos(x)
plt.plot(x, y1, '-r', label='sin(x)')    #指定資料之圖例標籤
plt.plot(x, y2, ':b', label='cos(x)')    #指定資料之圖例標籤
plt.legend()                               #顯示圖例
plt.title('functions')                   #設定圖形標題
plt.xlabel('X')                           #設定 X 軸標籤
plt.ylabel('Y')                           #設定 Y 軸標籤
plt.fill_between(x, y1, y2, color='yellow')
plt.show()
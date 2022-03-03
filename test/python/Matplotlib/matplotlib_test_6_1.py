import numpy as np
import matplotlib.pyplot as plt 
x=np.arange(0,10)                    #X 軸
y1=x                                 #Y軸1=x
y2=x**2                              #Y軸2=x**2
plt.plot(x, y1, 'r--o', label='x')   #指定資料之圖例標籤
plt.plot(x, y2, 'b:d', label='x**2') #指定資料之圖例標籤
plt.legend()                         #顯示圖例
plt.title('functions')               #設定圖形標題
plt.xlabel('X')                      #設定 X 軸標籤
plt.ylabel('Y')                      #設定 Y 軸標籤
plt.show()
import numpy as np
import matplotlib.pyplot as plt
#plt.figure(figsize=[8, 4])
plt.axes([0.05, 0.05, 0.4, 0.95])
x=np.linspace(-5, 5, 100)
y=x                                    # 在 (2, 1, 1) 子圖上繪製函數 y=x
plt.title('y=x')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)

plt.axes([0.55, 0.05, 0.4, 0.95])                 # 定位 (2, 1, 2) 子圖
y=x**2                               # 在 (2, 1, 2) 子圖上繪製函數 y=x
plt.title('y=x**2')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)    
plt.show()
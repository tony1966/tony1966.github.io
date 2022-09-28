import matplotlib.pyplot as plt  
import numpy as np 
x=np.linspace(0, 10, 100) 
fig=plt.figure()   
ax1=fig.add_axes([0.1, 0.6, 0.8, 0.3])  
ax2=fig.add_axes([0.1, 0.1, 0.8, 0.3])   
ax1.plot(x, np.sin(x))   
ax2.plot(x, np.cos(x))    
ax1.set_title('Function of Sin(x)')    
ax2.set_title('Function of Cos(x)')    
plt.show()                 
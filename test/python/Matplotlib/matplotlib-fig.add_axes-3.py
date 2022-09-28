import matplotlib.pyplot as plt  
import numpy as np 
fig=plt.figure(figsize=[10, 8])            
x=np.linspace(0, 2*np.pi, 360)              
ax1=fig.add_axes([0.1, 0.1, 0.8, 0.8])     
ax1.plot(x, np.sin(x))
ax2=fig.add_axes([0.55, 0.55, 0.3, 0.3])     
ax2.plot(x, np.cos(x))    
ax1.set_title('Function of Sin(x)')      
ax2.set_title('Function of Cos(x)')         
plt.show()              
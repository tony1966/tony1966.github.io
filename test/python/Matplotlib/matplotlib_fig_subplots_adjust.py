import matplotlib.pyplot as plt  
import numpy as np

x=np.linspace(0, 10, 100)     
fig=plt.figure()
fig.subplots_adjust(0.2, 0.2)
ax1=fig.add_subplot(211)       
ax1.plot(x, np.sin(x))    
ax1.set_title('Sin function')     
ax2=fig.add_subplot(212)     
ax2.plot(x, np.cos(x))            
ax2.set_title('Cos function')     
plt.tight_layout() 
plt.show()      
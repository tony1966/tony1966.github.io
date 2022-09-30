import matplotlib.pyplot as plt  
import numpy as np

x=np.linspace(0, 2*np.pi)               
fig=plt.figure()    
ax1=fig.add_subplot(231)   
ax1.plot(x, np.sin(x)) 
ax1.set_title('Sin(x)')
ax2=fig.add_subplot(235)      
ax2.plot(x, np.cos(x))  
ax2.set_title('Cos(x)') 
ax3=fig.add_subplot(236)      
ax3.plot(x, np.tan(x))   
ax3.set_title('Tan(x)') 
ax4=fig.add_subplot(233)
plt.tight_layout()
plt.show()


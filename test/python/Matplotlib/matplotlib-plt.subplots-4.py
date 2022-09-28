import matplotlib.pyplot as plt  
import numpy as np   

x=np.linspace(0, 10, 100)      
fig, ax=plt.subplots(2, 1, sharex=True)      
ax[0].plot(x, np.sin(x))        
ax[1].plot(x, np.cos(x))    
ax[0].set_title('Sin(x)')   
ax[1].set_title('Cos(x)')     
plt.show()           
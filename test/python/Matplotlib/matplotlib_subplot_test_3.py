import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)
plt.subplot(121)
y=x
plt.title('y=x')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)
plt.subplot(122)
y=x**2
plt.title('y=x**2')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)    
plt.show()
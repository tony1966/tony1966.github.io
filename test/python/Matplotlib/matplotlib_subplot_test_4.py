import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)
plt.subplot(221)
y=x
plt.title('y=x')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)
plt.subplot(222)
y=x**2
plt.title('y=x**2')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)
plt.subplot(223)
y=x**3
plt.title('y=x**3')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)
plt.subplot(224)
y=x**4
plt.title('y=x**4')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)    
plt.show()
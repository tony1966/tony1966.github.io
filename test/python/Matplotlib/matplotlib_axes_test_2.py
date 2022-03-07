import numpy as np
import matplotlib.pyplot as plt
plt.axes()
x=np.linspace(-5, 5, 100)
y=x                                    
plt.title('y=x')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)

plt.axes([0.55, 0.2, 0.3, 0.3])                
y=x**2                              
plt.title('y=x**2')                      
plt.xlabel('x')                                                 
plt.ylabel('y') 
plt.plot(x, y)    
plt.show()
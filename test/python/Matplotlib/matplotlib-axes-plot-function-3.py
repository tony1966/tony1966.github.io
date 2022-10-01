import matplotlib.pyplot as plt  
import numpy as np 

fig=plt.figure()   
ax=fig.add_subplot()   
x=np.arange(3)   
ax.plot(x, -x**2, x, -x**3, x, -2*x, x, -2**x)
ax.set(xlabel='x', ylabel='y = f(x)', title='Plotting of Function')
ax.legend(['-x**2', '-x**3', '-2*x', '-2**x'])
ax.grid(True)
ax.text(0.25, -5, "Object Oriented Plotting")
plt.show()
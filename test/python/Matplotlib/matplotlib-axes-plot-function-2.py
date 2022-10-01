import matplotlib.pyplot as plt  
import numpy as np 

fig=plt.figure()   
ax=fig.add_subplot()   
x=np.arange(3)   
ax.plot(x, -x**2, label='-x**2')
ax.plot(x, -x**3, label='-x**3')
ax.plot(x, -2*x, label='-2*x')
ax.plot(x, -2**x, label='-2**x')
ax.set(xlabel='x', ylabel='y = f(x)', title='Plotting of Function')
ax.legend()
ax.grid(True)
ax.text(0.25, -5, "Object Oriented Plotting")
plt.show()
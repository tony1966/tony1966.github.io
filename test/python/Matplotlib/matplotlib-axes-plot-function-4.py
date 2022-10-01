import matplotlib.pyplot as plt  
import numpy as np 

fig=plt.figure()   
ax=fig.add_subplot()   
x=np.linspace(0, 2*np.pi)   
ax.plot(x, np.sin(x), x, np.cos(x))
ax.set(xlabel='x',
       ylabel='y = f(x)',
       title='sin(x) and cos(x)',
       xticks=[0, np.pi*0.5, np.pi, np.pi*1.5, np.pi*2],
       xticklabels=['0°', '90°', '180°', '270°', '360°'])
ax.legend(['y=sin(x)', 'y=cos(x)'])
ax.grid(True)
plt.show()
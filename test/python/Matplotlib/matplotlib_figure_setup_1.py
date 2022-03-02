import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=[8, 6],
           dpi=120,
           facecolor='cyan',
           edgecolor='blue',
           linewidth=5,
           frameon=False)
x=np.linspace(-5, 5, 100)
y=x**2
plt.title('y=x**2')
plt.xlabel('x')                                                 
plt.ylabel('y')
plt.plot(x, y)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 10, 100)
y1=x**2
y2=x
plt.plot(x, y1, 'red', x, y2, 'blue')
plt.fill_between(x, y1, y2, color='yellow')
plt.show()
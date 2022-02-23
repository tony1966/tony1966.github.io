import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 10, 100)
y1=x**2
plt.plot(x, y1)
plt.fill_between(x, y1)
plt.show()
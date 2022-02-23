import numpy as np
import matplotlib.pyplot as plt

y=np.linspace(0, 100, 100)
x1=np.sqrt(y)
x2=y
plt.plot(x1, y, color='red')
plt.plot(x2, y, color='blue')
plt.fill_betweenx(y, x1, x2, color='yellow')
plt.show()
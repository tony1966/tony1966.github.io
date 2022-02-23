import numpy as np
import matplotlib.pyplot as plt

y=np.linspace(0, 100, 100)
x1=np.sqrt(y)
plt.plot(x1, y, color='red')
plt.fill_betweenx(y, x1)
plt.show()
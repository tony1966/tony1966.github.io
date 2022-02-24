import numpy as np
import matplotlib.pyplot as plt

x=np.arange(5)
y=x
plt.plot(x, y, '-')
plt.plot(x, y + 1 , '--')
plt.plot(x, y + 2, '-.')
plt.plot(x, y + 3, ':')
plt.show()

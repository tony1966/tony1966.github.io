import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.01, 10, 100)
y=np.sin(2 * np.pi * x)
plt.loglog(x, y)
plt.show()
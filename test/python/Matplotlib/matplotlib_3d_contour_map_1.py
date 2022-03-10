import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

ax=plt.axes(projection='3d')
x=np.linspace(-2, 2, 20)
y=np.linspace(-2, 2, 20)
#X, Y=np.meshgrid(x, y)
X, Y=np.mgrid[-2:2:20j, -2:2:20j]
Z=X * np.exp(- X ** 2 - Y ** 2)
surface=ax.plot_surface(X, Y, Z, rstride=2, cstride=1, cmap=plt.cm.Blues_r)
plt.colorbar(surface, shrink=0.5, aspect=10)
plt.show()
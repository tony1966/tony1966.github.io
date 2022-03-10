import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

ax=plt.axes(projection='3d')
x=np.linspace(-2, 2, 20)
y=np.linspace(-2, 2, 20)
X, Y=np.meshgrid(x, y)
Z=np.sin(np.sqrt(X**2 + Y**2))
surface=ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm)
plt.colorbar(surface, shrink=0.5, aspect=10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
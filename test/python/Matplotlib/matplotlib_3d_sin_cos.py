import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

ax=plt.axes(projection='3d')
x=np.linspace(0, 20, 100)
y=np.sin(x)
z=np.cos(x)
ax.plot3D(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('plot3D(x, sin(x), cos(x))')
plt.show()
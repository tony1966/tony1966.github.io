import matplotlib.pyplot as plt  
import numpy as np

np.random.seed(42)
x=np.random.randn(1000)
y=np.random.randn(1000)
fig=plt.figure() 
grid=fig.add_gridspec(nrows=2, ncols=2, wspace=0.05, hspace=0.05)
ax=fig.add_subplot(grid[1, 0])
ax_histx=fig.add_subplot(grid[0, 0])
ax_histy=fig.add_subplot(grid[1, 1])
ax_histx.set_xticklabels([])
ax_histy.set_yticklabels([])
ax.scatter(x, y)
ax_histx.hist(x, bins=10)
ax_histy.hist(y, bins=10, orientation='horizontal')
plt.show()
import matplotlib.pyplot as plt  

fig=plt.figure(constrained_layout=True)
grid=fig.add_gridspec(nrows=2, ncols=3)
ax1=fig.add_subplot(grid[0, 0])
ax2=fig.add_subplot(grid[0, 1:])
ax3=fig.add_subplot(grid[1, :2])
ax4=fig.add_subplot(grid[1, 2])
plt.show()             
import matplotlib.pyplot as plt  

fig=plt.figure(constrained_layout=True) 
grid=fig.add_gridspec(nrows=3, ncols=3)
ax1=fig.add_subplot(grid[0, :])
ax2=fig.add_subplot(grid[1, :-1])
ax3=fig.add_subplot(grid[2, 0])
ax4=fig.add_subplot(grid[2, 1])
ax5=fig.add_subplot(grid[1:, 2])
plt.show()
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec  

fig=plt.figure()
grid=gridspec.GridSpec(2, 3, wspace=0.4, hspace=0.4)
ax1=fig.add_subplot(grid[0, 0])
ax2=fig.add_subplot(grid[0, 1:])
ax3=fig.add_subplot(grid[1, :2])
ax4=fig.add_subplot(grid[1, 2])
plt.show()             
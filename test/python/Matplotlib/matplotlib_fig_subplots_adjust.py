import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax1=fig.add_subplot(2, 1, 1)
ax2=fig.add_subplot(212)
ax1.plot(np.random.randn(10))
ax2.plot(np.random.randn(10))
fig.set_size_inches(5, 4)
fig.set_facecolor('cyan')
plt.show()
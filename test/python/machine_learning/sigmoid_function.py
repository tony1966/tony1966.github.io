import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

plt.title('Sigmoid Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y=sigmoid(x)
plt.plot(x, y)
plt.show()
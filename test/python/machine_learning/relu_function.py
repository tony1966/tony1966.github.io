import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

plt.title('ReLU Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y=relu(x)
plt.plot(x, y)
plt.show()
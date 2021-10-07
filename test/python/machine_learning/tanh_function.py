import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return np.tanh(x)

plt.title('Tanh Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y=tanh(x)
plt.plot(x, y)
plt.show()
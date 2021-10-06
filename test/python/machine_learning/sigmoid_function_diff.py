import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_diff(x):
    return sigmoid(x) * (1 - sigmoid(x))

plt.title('Sigmoid Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y=sigmoid_diff(x)
plt.plot(x, y)
plt.show()
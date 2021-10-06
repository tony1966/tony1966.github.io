import numpy as np
import matplotlib.pyplot as plt

def sigmoid_function(x):
    return 1/(1 + np.exp(-x))

plt.title('Sigmoid Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y=sigmoid_function(x)
plt.plot(x, y)
plt.show()
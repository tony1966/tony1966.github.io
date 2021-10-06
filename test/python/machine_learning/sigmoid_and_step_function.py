import numpy as np
import matplotlib.pyplot as plt

def step(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

plt.title('Sigmoid & Step Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y1=sigmoid(x)
y2=step(x)
plt.plot(x, y1, 'b-', x, y2, 'r--')
plt.show()
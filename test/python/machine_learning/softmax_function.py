import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    return np.exp(x)/sum(np.exp(x))

plt.title('Softmax Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y=softmax(x)
plt.plot(x, y)
plt.show()
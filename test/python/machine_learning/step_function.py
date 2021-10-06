import numpy as np
import matplotlib.pyplot as plt

def step(x):
    return np.array(x > 0, dtype=np.int)

plt.title('Step Function')
plt.xlabel('X')
plt.ylabel('Y')
x=np.arange(-5, 5, 0.1)
y=step(x)
plt.plot(x, y)
plt.show()
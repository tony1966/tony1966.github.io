import numpy as np

def softmax(x):
    return np.exp(x)/sum(np.exp(x))

x=np.array([1, 5, 2, 0, 6, 7])
y=softmax(x)
print(y)
print("Sum=", sum(y))
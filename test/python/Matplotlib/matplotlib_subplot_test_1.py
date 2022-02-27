import matplotlib.pyplot as plt

for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.3, 0.5, str((2, 3, i)))
plt.show()

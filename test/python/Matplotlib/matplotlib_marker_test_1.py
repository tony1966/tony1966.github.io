import matplotlib.pyplot as plt

markers=['.', ',', '*', '+', 'x', 'o', 's', 'p', 'D', 'd', 'h',
         'H', '^', 'v', '<', '>', '|', '_', '1', '2', '3', '4']
x=range(len(markers))
for i in x:
    plt.plot(i, i, markers[i])
plt.show()

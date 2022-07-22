import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set()
df=sns.load_dataset('flights')
sns.lineplot(x='year', y='passengers', hue='month', data=df)
plt.show()
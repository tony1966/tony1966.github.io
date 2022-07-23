import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set()
df=sns.load_dataset('flights')
sns.relplot(x='year', y='passengers', hue='month', kind='line', data=df)
plt.show()
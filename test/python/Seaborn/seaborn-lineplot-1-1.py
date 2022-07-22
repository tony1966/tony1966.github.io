import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=sns.load_dataset('flights')
sns.set()
sns.lineplot(x="year", y="passengers", data=df)
plt.show()
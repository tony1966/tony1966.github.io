import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=sns.load_dataset('flights')
flights_wide=df.pivot("year", "month", "passengers")
sns.set()
sns.lineplot(data=flights_wide)
plt.ylabel('passengers')
plt.show()
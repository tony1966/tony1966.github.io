import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set()
df=sns.load_dataset('flights')
flights_wide=df.pivot("year", "month", "passengers")
sns.lineplot(data=flights_wide, dashes=False)
plt.ylabel('passengers')
plt.show()
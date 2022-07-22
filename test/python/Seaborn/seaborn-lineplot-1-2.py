import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=sns.load_dataset('flights')
may_flights=df.query("month=='May'") 
sns.set()
sns.lineplot(x="year", y="passengers", data=may_flights)
plt.show()
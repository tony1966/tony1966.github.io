import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

election={'votes': [608590, 5522119, 8170231],
          'candidates': ['James Soong', 'Korea Fish', 'Tsai Ing-Wen']}
data=pd.DataFrame(election)
sns.set_style('dark', {'axes.edgecolor': 'blue', 'axes.facecolor': 'cyan'})
sns.barplot(x='candidates', y='votes', data=data)
plt.title('2020 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()
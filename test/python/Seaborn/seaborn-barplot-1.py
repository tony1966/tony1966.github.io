import seaborn as sns
import matplotlib.pyplot as plt

votes=[608590, 5522119, 8170231]
candidates=['James Soong', 'Korea Fish', 'Tsai Ing-Wen']
sns.barplot(x=candidates, y=votes)
plt.title('2020 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()
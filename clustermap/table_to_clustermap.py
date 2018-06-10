
import pandas as pd
import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt
import sys

df = pd.read_csv(sys.argv[1])

with open(sys.argv[2], encoding='utf-8-sig') as f:
    row_names = [line.strip() for line in f]

df = df.fillna(0)
df.index = row_names[0:df.shape[0]]
g = sns.clustermap(df, cmap='PuRd', figsize=(60, 200))
plt.savefig(sys.argv[3])



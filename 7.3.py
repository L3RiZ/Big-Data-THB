import pandas as pd 
import matplotlib.pyplot as plt

df_sets01 = pd.read_csv('./Lego/sets01.csv', delimiter=',')
df_sets02 = pd.read_csv('./Lego/sets02.csv', delimiter=',')
df_sets03 = pd.read_csv('./Lego/sets03.csv', delimiter=',')


df = pd.concat([df_sets01, df_sets02, df_sets03])

df['year'].value_counts(sort=False).plot(kind='bar', figsize=(10, 5))

plt.savefig('lego1.pdf')

print(df)
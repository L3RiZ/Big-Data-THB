import pandas as pd
import matplotlib.pyplot as plt

df_Hundehalter = pd.read_csv('20151001hundehalter.csv', delimiter=',')
df_Hunde = pd.read_csv('zuordnungstabellehunderassehundetyp.csv', delimiter=',')

df_Hundehalter.rename(columns={'RASSE1' : "HUNDERASSE"}, inplace=True)
df_Hundehalter.drop(columns=('RASSENTYP'), inplace=True)

df = pd.merge(df_Hunde, df_Hundehalter, on="HUNDERASSE", sort=True)

def rename(x):
    if x == False:
        return "Nicht spezifiert"
    else:
        return x

df['HUNDERASSENTYP'] = df['HUNDERASSENTYP'].apply(rename)

gr = df.groupby('HUNDERASSENTYP')['HUNDERASSE'].count()
cond = (df.HUNDERASSENTYP == "Rassentypenliste II")

a = df[cond]['ALTER']

a.value_counts(sort=False).plot(kind='bar')

plt.savefig('test.pdf')

print(a)

print(df[cond]['HUNDERASSE'].unique())


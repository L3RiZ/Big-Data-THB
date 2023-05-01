import pandas as pd
import matplotlib.pyplot as plt

#Aufgabe 6.2 b

df = pd.read_csv('20151001hundehalter.csv', delimiter=",")

#Aufgabe 6.2 c

# df.hist(column="ALTER")
# plt.savefig("ALTER.pdf")

df.hist(column="GEBURTSJAHR_HUND", bins=50, range=[1962, 2016], edgecolor='black')
plt.savefig("GEBURTSJAHR_HUND.pdf")

#Aufgabe 6.2 d

f = df.describe()

#Aufgabe 6.2 e

e = df.sort_values(by='GEBURTSJAHR_HUND').head(10)["RASSE1"]

#Aufgabe 6.2 f

cond1 = (df["ALTER"] == "11-20")
cond2 = (df["ALTER"] == "91-100")

print(df[cond2]["RASSE1"])


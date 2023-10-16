import pandas as pd
import matplotlib.pyplot as plt 

# Aufgabe 6.1 b

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=','
)

# Aufgabe 6.1 c

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=','
).head(11)

# Aufgabe 6.1 d

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=','
).tail(6)

# Aufgabe 6.1 e

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=',')[["Salary", "EmpSatisfaction"]].describe()

# Aufgabe 6.1 f

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=',').Employee_Name

# Aufgabe 6.1 g

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=',')

cond = (df.CitizenDesc != "US Citizen")

print(df[cond].Employee_Name)

# Aufgabe 6.1 h

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=','
).sort_values(by='Salary', ascending=False).Employee_Name.head(15)

# Aufgabe 6.1 i

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=',')

cond = ((df.EmpID > 10100) & (df.EmpID < 10150))

f = df[cond]

print(f)

# Aufgabe 6.1 j

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=','
).sort_values(by="EmpID").iloc[9:19]

print(df)

# Aufgabe 6.1 k

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=','
)

df.hist(column="EmpSatisfaction")
plt.savefig('EmpSatisfaction.pdf')
df.hist(column="Absences", bins=20)
plt.savefig('Absences.pdf')
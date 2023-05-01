import pandas as pd

# Aufgabe 6.1 b

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=','
# )

# Aufgabe 6.1 c

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=','
# ).head(11)

# Aufgabe 6.1 d

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=','
# ).tail(6)

# Aufgabe 6.1 e

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=',').Salary.describe()

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=',').EmpSatisfaction.describe()

# Aufgabe 6.1 f

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=',').Employee_Name

# Aufgabe 6.1 g

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=',')

# cond = (df.CitizenDesc != "US Citizen")

# print(df[cond].Employee_Name)

# Aufgabe 6.1 h

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=','
# ).sort_values(by='Salary', ascending=False).Employee_Name.head(15)

# Aufgabe 6.1 i

# df = pd.read_csv(
#     'HRDataset_v14 (1).csv', delimiter=',')

# cond = ((df.EmpID > 10100) & (df.EmpID < 10150))

# f = df[cond]

# print(f)

# Aufgabe 6.1 j
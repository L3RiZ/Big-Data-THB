import pandas as pd

df = pd.read_csv(
    'HRDataset_v14 (1).csv', delimiter=',', usecols=['Salary', 'Employee_Name', 'EmpSatisfaction', 'Position', 'PositionID', 'EmpID',]  
)

def minmax(x):
    return (x - 1) * 1 / 4



df['SalaryThousands'] = df['Salary'] / 1000
df['EmpSatisfaction'] = df['EmpSatisfaction'].apply(minmax)
df.drop(inplace=True, columns=['Position', 'PositionID'])
df.set_index('EmpID', inplace=True)
df.drop(inplace=True, index=[10066, 10226, 10181])



print(df)

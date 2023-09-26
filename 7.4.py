import pandas as pd

df = pd.read_csv('AirPassengersMissing.csv', delimiter=',')
df['#Passengers'].fillna(method=('bfill'), inplace=True)

# Welche ist am besten geeignet? 

print(df)
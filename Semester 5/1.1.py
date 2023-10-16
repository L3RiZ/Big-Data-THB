import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score

df = pd.read_csv('./Semester 5/housing.csv', delimiter=',')
df['median_rooms'] = df['total_rooms'] / df['households']
df['median_bedrooms'] = df['total_bedrooms'] / df['households']
df['population_per_household'] = df['population'] / df['households']
df['median_bedrooms'].fillna(inplace=True, value=df['median_bedrooms'].dropna().median())
df.drop(inplace=True, columns=['total_rooms', 'total_bedrooms', 'population', 'ocean_proximity'])

data_cols = ['longitude', 'latitude', 'housing_median_age', 'households', 'median_income', 'median_rooms', 'median_bedrooms', 'population_per_household']

train, test = np.split(df.sample(frac=1), [int(0.75*len(df))])

def split_data(dataframe):
    X = dataframe.loc[:, data_cols]
    y = dataframe['median_house_value']
    
    return dataframe, X, y

train, X_train, y_train = split_data(train)
test, X_test, y_test = split_data(test)

print('Linear model')
model = LinearRegression()
print('Train R2: {}'.format(r2_score(y_train, model.fit(X_train, y_train).predict(X_train))))
print('Test R2: {}'.format(r2_score(y_test, model.fit(X_train, y_train).predict(X_test))))
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
print('Scores: {}'.format(scores))
print('Mean score: {}'.format(scores.mean()))
print('Std score: {}'.format(scores.std()))
print()
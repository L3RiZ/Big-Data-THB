import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

if __name__ == '__main__':
    df = pd.read_csv('./Semester 5/housing.csv', delimiter=',')
    df['median_rooms'] = df['total_rooms'] / df['households']
    df['median_bedrooms'] = df['total_bedrooms'] / df['households']
    df['population_per_household'] = df['population'] / df['households']
    df['median_bedrooms'].fillna(inplace=True, value=df['median_bedrooms'].dropna().median())
    df.drop(inplace=True, columns=['total_rooms', 'total_bedrooms', 'population', 'ocean_proximity'])
    

    data_cols = ['longitude', 'latitude', 'housing_median_age', 'households', 'median_income', 'median_rooms', 'median_bedrooms', 'population_per_household']
    X = df.loc[:, data_cols]
    y = df['median_house_value']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, shuffle=True)

    print('Linear model')
    model = LinearRegression()
    print('Train R2: {}'.format(r2_score(y_train, model.fit(X_train, y_train).predict(X_train))))
    print('Test R2: {}'.format(r2_score(y_test, model.fit(X_train, y_train).predict(X_test))))
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
    print('Scores: {}'.format(scores))
    print('Mean score: {}'.format(scores.mean()))
    print('Std score: {}'.format(scores.std()))
    print()

    print('Quadratic model')
    X_train_poly = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X_train)
    X_test_poly = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X_test)
    model = LinearRegression()
    print('Train R2: {}'.format(r2_score(y_train, model.fit(X_train_poly, y_train).predict(X_train_poly))))
    print('Test R2: {}'.format(r2_score(y_test, model.fit(X_train_poly, y_train).predict(X_test_poly))))
    scores = cross_val_score(model, X_train_poly, y_train, cv=5, scoring='r2')
    print('Scores: {}'.format(scores))
    print('Mean score: {}'.format(scores.mean()))
    print('Std score: {}'.format(scores.std()))
    print()

    print('Random Forest Regressor')
    model = RandomForestRegressor()
    print('Train R2: {}'.format(r2_score(y_train, model.fit(X_train, y_train).predict(X_train))))
    print('Test R2: {}'.format(r2_score(y_test, model.fit(X_train, y_train).predict(X_test))))
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
    print('Scores: {}'.format(scores))
    print('Mean score: {}'.format(scores.mean()))
    print('Std score: {}'.format(scores.std()))
    print()

# script used to test the algorithms

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import model_selection, metrics
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('../dataset/winequality-red.csv')

x = df.loc[:, df.columns != 'quality']
y = df['quality']
len(x.columns)
n_neighbors = len(y.unique())

sc_x = StandardScaler()
xscaled = sc_x.fit_transform(x)

xtrain, xtest, ytrain, ytest = model_selection.train_test_split(xscaled, y)


# model = SVC(gamma='auto', kernel='rbf')
model = RandomForestClassifier(n_estimators=50)
# model = KNeighborsClassifier(n_neighbors=n_neighbors)
# model = SVR(kernel='rbf', epsilon=0.001, gamma=30)

model.fit(xtrain, ytrain)

ypred_train = model.predict(xtrain)
ypred_test = model.predict(xtest)

print(model.score(xtest, ytest))
print(model.score(xtrain, ytrain))
# print(x.columns)
# print(sc_x.inverse_transform(xtest), ypred_test)
# print(metrics.classification_report(ytest, ypred_test))


# param = {
#     'C': [0.1, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4],
#     'kernel':['linear', 'poly', 'rbf'],
#     'degree': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
#     'coef0' :[0.1, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4],
#     'gamma' :[0.1, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4]
# }
# grid_svc = model_selection.GridSearchCV(model, param_grid=param, scoring='accuracy', cv=10)

# grid_svc.fit(xtrain, ytrain)

# print(grid_svc.best_params_)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import joblib

from sklearn import model_selection, metrics
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.externals import joblib

df = pd.read_csv('../dataset/winequality-red.csv')

x = df.loc[:, df.columns != 'quality']
y = df['quality']

# df[['quality', 'pH']].plot.bar()

# x = np.asanyarray(x).reshape(-1, 1)
# y = np.asanyarray(y).reshape(-1, 1)
sc_x = StandardScaler()
xscaled = sc_x.fit_transform(x)

xtrain, xtest, ytrain, ytest = model_selection.train_test_split(xscaled, y)

# model = RandomForestClassifier(n_estimators=50)
model = SVC(gamma='auto', kernel='rbf')

model.fit(xtrain, ytrain)

print(model.score(xtest, ytest))
print(model.score(xtrain, ytrain))

joblib.dump(model, '../models/model-sk22.joblib')
joblib.dump(sc_x, '../models/model-scaler-sk22.joblib')

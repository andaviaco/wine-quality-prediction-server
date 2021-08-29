import numpy as np
from sklearn.externals import joblib

model = joblib.load('../model/model.joblib')
scaler = joblib.load('../model/model-scaler.joblib')

def predict(raw_values):
  values = (np.array(raw_values)).reshape(1, -1)
  scaled_values = scaler.transform(values)

  predicted = model.predict(scaled_values)

  return predicted
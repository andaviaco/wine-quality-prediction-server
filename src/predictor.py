import numpy as np
from sklearn.externals import joblib

model = joblib.load('../model/model-sk22-latest.joblib')
scaler = joblib.load('../model/model-scaler-sk22-latest.joblib')

def predict(raw_values):
  values = (np.array(raw_values)).reshape(1, -1)
  scaled_values = scaler.transform(values)

  predicted = model.predict(scaled_values)

  return predicted
#Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
#Data
df = pd.read_csv('dogec.csv')

#Variable to predict price for N days
prediction_days = 30

#for n units
df['Prediction'] = df[['Price']].shift(-prediction_days)

#create independent data sset
x = np.array(df.drop(['Prediction'],1))

x = x[:len(df)-prediction_days]

#convert dataframe into array
y= np.array(df['Prediction'])

#all values except for last 30 rows
y = y[:-prediction_days]

#SPLITTING DATA: Training data (80%) $ testing data (20%)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

#Set prediction_days_array = last 30 days data from original data Set
prediction_days_array = np.array(df.drop(['Prediction'],1))[-prediction_days:]

#Creating & training SVR machine (radial basis function)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.00001)
svr_rbf.fit(x_train, y_train)

SVR(C=1000.0 , cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=1e-05, kernel= 'rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

#Test
svr_rbf_confidence = svr_rbf.score(x_test , y_test)
print("svr_rbf accuracy:" , svr_rbf_confidence)

#Getting Predicted And Actual Values
svm_prediction = svr_rbf.predict(prediction_days_array)
print(svm_prediction)
print("*******************")
print("Actual Value:")
print(df.tail(prediction_days))

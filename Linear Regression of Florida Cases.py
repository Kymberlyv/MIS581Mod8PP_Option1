import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os
os.chdir("/Users/kymberlyvanlaar/Desktop")
american = '2020americanout.xlsx'
xl = pd.ExcelFile(american)
df = xl.parse('Sheet1')
X = df['MIA_cases'].values.reshape(-1,1)
Y = df['MIA'].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, Y_train) #training the algorithm
LinearRegression()
print(regressor.intercept_)
print(regressor.coef_)
Y_pred = regressor.predict(X_test)
df1 = pd.DataFrame({'Actual': Y_test.flatten(), 'Predicted': Y_pred.flatten()})
df1
df2.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
plt.scatter(X_test, Y_test,  color='gray')
plt.plot(X_test, Y_pred, color='red', linewidth=2)
plt.show()
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_pred))
Mean Absolute Error: 5.770940180135696
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, Y_pred))
Mean Squared Error: 83.90537855846033
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)))
Root Mean Squared Error: 9.159987912571737


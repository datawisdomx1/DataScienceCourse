#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:23:29 2020

@author: nitinsinghal
"""

# Chapter 8 - Supervised Learning - Regression
# Regularization (Ridge, Lasso) Regression - Interest rate and other macroeconomic data for US

#Import libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Use the data science process steps given in chapter 6 to build the Regularization regression model
# Data being already cleaned requires minimal pre-processing

# Import inflation and interest rate data for US
usmacro10yrpriceyielddata = pd.read_csv('/Users/nitinsinghal/Dropbox/DataScienceCourse/Data/USMacro10yrPriceYield.csv')

# Split the data into depdendent y and independent X variables
X = usmacro10yrpriceyielddata.iloc[:, 1:7].values
y = usmacro10yrpriceyielddata.iloc[:, 7].values

# As y is a 1 dimensional array, and the algorithm expects a 2D array
# we need to reshape the array. Using numpy reshape method this can be done easily
y = y.reshape(-1,1)

# Split the data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

# Create the Ridge regressor - L2 regularization
estimator = Ridge(alpha=0.1)

# Fit the estimator to the training data to build the model
estimator.fit(X_train, y_train)

# Using the estimator predict y values using the X test data 
y_pred = estimator.predict(X_test)

# Calculate error metrics for predicted y values vs y test data
mse = mean_squared_error(y_test , y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test , y_pred)
r2 = r2_score(y_test , y_pred)
print('MSE:%.4f, RMSE:%.4f, MAE:%.4f, R2:%.4f' %(mse, rmse, mae, r2))
plt.title('Multi-linear Regression - 10yr Bond Price vs Macroeconomic factors')
plt.xlabel('Macroeconomic factors')
plt.ylabel('10yr Bond Price')
plt.plot(y_test, color='red', label='Actual values')
plt.plot(y_pred, color='blue', label='Predicted values')
plt.legend()
plt.show()

# Validate the model by predicting the y value for a given X values 
X_validate = usmacro10yrpriceyielddata.iloc[221:222, 1:7].values
y_validate = usmacro10yrpriceyielddata.iloc[221:222, 7].values
y_validate_pred = estimator.predict(X_validate)

print('X value: ', X_validate, 'Predicted y value: ', y_validate_pred, 'Actual y value: ', y_validate, 
      'y Pred - Actual: ', (y_validate_pred-y_validate), 'y diff %: ', ((y_validate_pred-y_validate)/y_validate_pred)*100)

#######################################################################################
# Create the Lasso regressor - L1 regularization
estimator = Lasso(alpha=0.1)

# Fit the estimator to the training data to build the model
estimator.fit(X_train, y_train)

# Using the estimator predict y values using the X test data 
y_pred = estimator.predict(X_test)

# Calculate error metrics for predicted y values vs y test data
mse = mean_squared_error(y_test , y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test , y_pred)
r2 = r2_score(y_test , y_pred)
print('MSE:%.4f, RMSE:%.4f, MAE:%.4f, R2:%.4f' %(mse, rmse, mae, r2))
plt.title('Multi-linear Regression - 10yr Bond Price vs Macroeconomic factors')
plt.xlabel('Macroeconomic factors')
plt.ylabel('10yr Bond Price')
plt.plot(y_test, color='red', label='Actual values')
plt.plot(y_pred, color='blue', label='Predicted values')
plt.legend()
plt.show()


# Validate the model by predicting the y value for a given X values 
X_validate = usmacro10yrpriceyielddata.iloc[221:222, 1:7].values
y_validate = usmacro10yrpriceyielddata.iloc[221:222, 7].values
y_validate_pred = estimator.predict(X_validate)

print('X value: ', X_validate, 'Predicted y value: ', y_validate_pred, 'Actual y value: ', y_validate, 
      'y Pred - Actual: ', (y_validate_pred-y_validate), 'y diff %: ', ((y_validate_pred-y_validate)/y_validate_pred)*100)

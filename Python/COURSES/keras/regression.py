import pandas as pd
import numpy as np

#	Downloading the data
concrete_data = pd.read_csv('https://ibm.box.com/shared/static/svl8tu7cmod6tizo6rk0ke4sbuhtpdfx.csv')
print(concrete_data.head())

#	Shape	
print(concrete_data.shape)
#	Let's check the missing values
print(concrete_data.describe())
#	Sum of nulls per rows
print(concrete_data.isnull().sum())

# Splitting the dataset 
concrete_data_columns = concrete_data.columns
predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']] # all columns except Strength
target = concrete_data['Strength'] # Strength column

# Prooving that is good
print(predictors.head())
print(target.head())

#	Normalized Predictors
predictors_norm = (predictors - predictors.mean()) / predictors.std()
predictors_norm.head()

n_cols = predictors_norm.shape[1] # number of predictors

# Let's start building our networks
import keras 
from keras.models import Sequential
from keras.layers import Dense

# define regression model
def regression_model():
    # create model
    model = Sequential()
    model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))
    
    # compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# build the model
model = regression_model()

# fit the model
modelo = model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import tensorflow as tf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 6)

#	Defining some numbers
X = np.arange(0.0, 5.0, 0.1)
#print(X)

##You can adjust the slope and intercept to verify the changes in the graph
a = 1
b = 0

Y= a * X + b 
'''
plt.plot(X, Y) 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()'''

# ===========================================================================
# Linear Regression with TensorFlow
# ===========================================================================
# 
#!wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv
df = pd.read_csv("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv")

# take a look at the dataset
print(df.head())


#Lets say we want to use linear regression to predict Co2Emission 
# of cars based on their engine size. So, lets define X and Y value for the linear regression, that is, train_x and train_y:
train_x = np.asanyarray(df[['ENGINESIZE']])
train_y = np.asanyarray(df[['CO2EMISSIONS']])

a = tf.Variable(20.0)
b = tf.Variable(30.2)
y = a * train_x + b

#This function finds the mean of a multidimensional tensor, and the result can have a different dimension.
loss = tf.reduce_mean(tf.square(y - train_y))

print(loss)
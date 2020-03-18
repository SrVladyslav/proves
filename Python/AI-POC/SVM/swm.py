import pandas as pd

# Data Frame
df = pd.read_csv('Iris.csv')

# Deleting the ID column
df = df.drop(['Id'],axis=1)

# Selecting the Species column
tg = df['Species']

# Looking for the different types of elements into this column
s = set()
for val in tg:
	s.add(val)
s = list(s)

# Dropping the last 50 rows
rows = list(range(100,150))
df = df.drop(df.index[rows])

# Let's now plot our data
import matplotlib.pyplot as plt

x = df['SepalLengthCm']
y = df['PetalLengthCm']

setosa_x = x[:50]
setosa_y = y[:50]
versicolor_x = x[50:]
versicolor_y = y[50:]

plt.figure(figsize=(5,5))
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')
plt.title('SVM')
plt.scatter(setosa_x,setosa_y, marker='.', color='red')
plt.scatter(versicolor_x, versicolor_y, marker='+', color='blue')
#plt.show()

# Splitting data for train and test (90-10)
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Drops the rest of the features and extract the target values
df = df.drop(['SepalWidthCm','PetalWidthCm'],axis= 1)

Y = []
# Data labels
tg = df['Species']
for v in tg:
	if(v == 'Iris-setosa'):
		Y.append(-1)
	else:
		Y.append(1)
df = df.drop(['Species'], axis= 1)
X = df.values.tolist()

# Shuffling and splitting data into training and test set
X, Y = shuffle(X,Y)
x_train = []
y_train = []
x_test = []
y_test = []

# Preparing data
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size= 0.9)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

y_train = y_train.reshape(90,1)
y_test = y_test.reshape(10,1)

# Building a Support Vector Machine model with numpy
# ====================================================
train_f1 = x_train[:,0].reshape(90,1)
train_f2 = x_train[:,1].reshape(90,1)

# Parameters
w1 = np.zeros((90,1))
w2 = np.zeros((90,1))

epochs = 1
alpha = 0.0001

# Training
while(epochs < 100):
	y = w1*train_f1 + w2*train_f2
	prod = y * y_train
	count = 0
	#print("Epoch: ",epochs)
	for v in prod:
		if(v >= 1):
			cost = 0
			# Lambda = 1/epochs
			w1 = w1 - alpha * (2 * 1/epochs * w1)
			w2 = w2 - alpha * (2 * 1/epochs * w2)
		else:
			cost = 1 -v
			w1 = w1 + alpha * (train_f1[count] * y_train[count] - 2 * 1/epochs *w1)
			w2 = w2 + alpha * (train_f2[count] * y_train[count] - 2 * 1/epochs *w2)
		count += 1
	epochs += 1


# Testing the accuracy
from sklearn.metrics import accuracy_score

ind = list(range(10,90))
w1 = np.delete(w1, ind).reshape(10,1)
w2 = np.delete(w2, ind).reshape(10,1)

# Extracting the test features
test_f1 = x_test[:,0].reshape(10,1)
test_f2 = x_test[:,1].reshape(10,1)

# Prediction 
y_prediction = w1 * test_f1 + w2 * test_f2
predictions = []

for val in y_prediction:
	if(val > 1):
		predictions.append(1)
	else:
		predictions.append(-1)

print("=======================")
print("Accuracy: ",accuracy_score(y_test,predictions))
print("=======================")
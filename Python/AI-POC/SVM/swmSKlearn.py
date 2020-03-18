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


# SVC model :O
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='linear')
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_test,y_pred))
# Loading data
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('train.csv')

# Create a target object
y = data.SalePrice

features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = data[features]

# Splitting into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X,y, random_state= 1)

# Model
iowa_model = DecisionTreeRegressor(random_state = 1)
# Fitting model
iowa_model.fit(train_X, train_y)

val_predictions = iowa_model.predict(val_X)

val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))



# Random forest model
from sklearn.ensemble import RandomForestRegressor

# Define the model. Set random_state to 1
rf_model = RandomForestRegressor(random_state=1)

# fit your model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of your Random Forest model on the validation data
melb_preds = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(melb_preds,val_y)

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))

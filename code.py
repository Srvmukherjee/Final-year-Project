import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, StackingRegressor
from sklearn.linear_model import LinearRegression
import warnings
import pickle

warnings.filterwarnings("ignore")

# Load your dataset
data = pd.read_csv('dataSet.csv')

# Specify features (X) and target variable (y)
X = data.drop('Avg pathloss(dB)', axis=1)
y = data['Avg pathloss(dB)']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Define base layer models
knn = KNeighborsRegressor()
dt = DecisionTreeRegressor()
gb = GradientBoostingRegressor()
rf = RandomForestRegressor()

# Train base models on the training data
knn.fit(X_train, y_train)
dt.fit(X_train, y_train)
gb.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Train the final estimator (linear regression) using predictions of base models
final_estimator = LinearRegression()
base_model_predictions_train = {
    'knn': knn.predict(X_train),
    'dt': dt.predict(X_train),
    'gb': gb.predict(X_train),
    'rf': rf.predict(X_train)
}
final_estimator_input_train = pd.DataFrame(base_model_predictions_train)
final_estimator.fit(final_estimator_input_train, y_train)

# Instantiate and train the stacking regressor
base_models = [('knn', knn), ('dt', dt), ('gb', gb), ('rf', rf)]
stacking_reg = StackingRegressor(estimators=base_models, final_estimator=final_estimator)
model = stacking_reg.fit(X_train, y_train)

# Save the model to disk
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load the model (example of how to load and use the model)
model = pickle.load(open('model.pkl', 'rb'))

# Example input data for prediction
# Assume the input values are provided from the website as follows
input_data = [int(x) for x in "2,4,930,66.7092,5.12441,0.133312,246".split(' ')]  # Node No, K Value, Frequency, Avg Signal Power (dBm), Delay, Packet Loss
input_array = np.array([input_data])

# Predict the pathloss for the example input data
prediction = model.predict(input_array)
print(f'Predicted Pathloss: {prediction[0]}')

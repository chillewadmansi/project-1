import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("student_scores.csv")

# Display first five rows
print(data.head())

# Define input and output
X = data[['StudyHours']]
y = data['Score']

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict scores
predictions = model.predict(X_test)

print("professsional project structure")

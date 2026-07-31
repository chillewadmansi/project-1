import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create Dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 50, 55, 65, 70, 75, 85, 90, 95]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Student Dataset")
print(df)

# Input (X) and Output (y)
X = df[["Study_Hours"]]
y = df["Marks"]

# Split Dataset into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression Model
model = LinearRegression()

# Train the Model
model.fit(X_train, y_train)

# Print Model Details
print("\nModel Trained Successfully!")
print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict Marks for Test Data
predictions = model.predict(X_test)

print("\nTesting Data Predictions")
for i in range(len(X_test)):
    print("Study Hours:", X_test.iloc[i, 0],
          "Actual Marks:", y_test.iloc[i],
          "Predicted Marks:", round(predictions[i], 2))

print("Model trained successfully")

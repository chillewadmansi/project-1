from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data
hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
marks = [20, 30, 40, 50, 60, 70, 80, 90]

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    hours, marks, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(x_train, y_train)

# Predict
prediction = model.predict([[5]])

print("Predicted Marks:", prediction[0])

print("ML fundamentals understood")

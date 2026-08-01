import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("student_scores.csv")

# Display dataset
print("Student Dataset")
print(data)

# Input (StudyHours) and Output (Score)
X = data[["StudyHours"]]
y = data["Score"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the test data
predictions = model.predict(X_test)

# Display Actual vs Predicted Scores
result = pd.DataFrame({
    "Study Hours": X_test["StudyHours"].values,
    "Actual Score": y_test.values,
    "Predicted Score": predictions
})

print("\nActual vs Predicted Scores")
print(result)

# Predict score for new input
hours = float(input("\nEnter study hours: "))

new_data = pd.DataFrame({
    "StudyHours": [hours]
})

predicted_score = model.predict(new_data)

print("\nPredicted Score:", round(predicted_score[0], 2))

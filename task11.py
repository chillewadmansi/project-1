import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_scores.csv")

# Input and Output
X = data[["StudyHours"]]
y = data["Score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction App
print("===== Student Score Prediction App =====")

hours = float(input("Enter Study Hours: "))

new_data = pd.DataFrame({"StudyHours": [hours]})
predicted_score = model.predict(new_data)

print("Predicted Score:", round(predicted_score[0], 2))

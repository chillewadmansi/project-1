import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_scores.csv")

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["StudyHours"], df["Score"])
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()

# Bar Chart
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Score"])
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Score")
plt.show()

# Line Chart
plt.figure(figsize=(6,4))
plt.plot(df["StudyHours"], df["Score"], marker='o')
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()

print("Basic charts created")

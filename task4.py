import pandas as pd

# Load the dataset
df = pd.read_csv("student_scores.csv")

# Display the dataset
print("Dataset:")
print(df)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Display information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

print("dataset loaded successfully")

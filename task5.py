import pandas as pd

# Load dataset
df = pd.read_csv("student_scores.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

# Dataset statistics
print("\nStatistics:")
print(df.describe())

# Save cleaned dataset
df.to_csv("cleaned_student_scores.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_student_scores.csv'")

print("clean dataset prepared")

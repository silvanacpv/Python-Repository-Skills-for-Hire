#Reading CSV files with joins
#By:   Silvana Paredes
#Date: 14/08/2025

import pandas as pd


# Step 1: Read CSV files
df_students = pd.read_csv("STUDENTS.csv")
df_grades   = pd.read_csv("GRADES.csv")
df_subjects = pd.read_csv("SUBJECTS.csv")

# Strip spaces from string columns to avoid mismatch
df_grades["SUBJECT_ID"] = df_grades["SUBJECT_ID"].str.strip()
df_subjects["SUBJECT_ID"] = df_subjects["SUBJECT_ID"].str.strip()


# Step 2: Merge students with grades using the same column name 'ID'
data = pd.merge(df_students, df_grades, on="ID", how="inner")


# Step 3: Merge the result with subjects using 'SUBJECT_ID'
full_data = pd.merge(data, df_subjects, on="SUBJECT_ID", how="inner")


# Step 4: Print all scores without AGE column
print("Scores:")
print(full_data.drop(columns=["AGE", "SUBJECT_ID"]))

# Step 5: Average grade by student
average = full_data.groupby("NAME")["GRADE"].mean().reset_index()
average = average.sort_values(by="GRADE", ascending=False)
print("\nAverage grade by student:")
print(average)

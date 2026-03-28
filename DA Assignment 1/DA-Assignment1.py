# ----------------------------------------------------------------
# Data Analytics + AI - Assignment 1
# Healthcare Data Analysis with Python
# Student ID: DA21106
# Name: Silvana Paredes
# ----------------------------------------------------------------

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ----------------------------------------------------------------
# Datasets:
# ----------------------------------------------------------------

patients_df = pd.DataFrame({
    'patient_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'age': [45, 62, 38, 55, 71, 49, 33, 58],
    'province': ['Nova Scotia', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island',
    'Newfoundland', 'Nova Scotia', 'New Brunswick', 'Nova Scotia'],
    'diagnosis': ['Diabetes', 'Hypertension', 'Diabetes', 'Asthma', 'Hypertension',
    'Diabetes', 'Asthma', 'Hypertension'],
    'treatment_duration': [30, 45, 28, np.nan, 60, 35, np.nan, 52],
    'readmission': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes']
})

outcomes_df = pd.DataFrame({
    'patient_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'treatment_type': ['Medication', 'Lifestyle Change', 'Medication', 'Therapy',
    'Medication', 'Lifestyle Change', 'Therapy', 'Medication'],
    'initial_blood_pressure': [145, 160, 152, np.nan, 168, 148, np.nan, 155],
    'final_blood_pressure': [128, 142, 135, np.nan, 149, 138, np.nan, 133],
    'patient_satisfaction': [8.5, 7.2, 9.0, 8.3, 6.8, 7.9, 9.2, 8.7]
})

print(patients_df)
print(outcomes_df)

# ----------------------------------------------------------------
# Part 1: NumPy Array Operations
# ----------------------------------------------------------------
# 1. Create a NumPy array from the 'age' column in the Patient Records dataset. Calculate and print:
# ----------------------------------------------------------------
age_np = patients_df['age'].to_numpy()
print("\nPart 1: NumPy Array Operations")

# A. Mean age
mean_age = np.mean(age_np)
print("Mean age:", mean_age)

# B. Median age
median_age = np.median(age_np)
print("Median age:", median_age)

# C. Standard deviation of ages
std_age = np.std(age_np)
print("Standard deviation:", std_age)

# ----------------------------------------------------------------
# 2. Create a 2D NumPy array containing patient_id, age, and
# treatment_duration (replace NULL with 0).
# Reshape this array to have 3 columns.
# ----------------------------------------------------------------

# Select the columns: patient_id, age, and treatment_duration
patients_2d_df = patients_df[['patient_id', 'age', 'treatment_duration']]

# Replace NULL with 0 in treatment_duration column
patients_2d_df = patients_2d_df.fillna(0)

# Convert to 2D NumPy array
patients_2d_np = patients_2d_df.to_numpy()

# Reshape the array to have 3 columns, where -1 means a flexible
# number of rows, and 3 means the number of columns
patients_2d_np = patients_2d_np.reshape(-1, 3)

# Convert back to DataFrame for better display
patients_2d_view_df = pd.DataFrame(
    patients_2d_np, columns=patients_2d_df.columns
)

print("\n2. Create a 2D NumPy array")
print(patients_2d_view_df)

# ----------------------------------------------------------------
# 3. Use NumPy to create a boolean mask identifying patients over 60 years old.
# Print the patient IDs that match this condition.
# ----------------------------------------------------------------
over_60_mask_np = age_np > 60

print("\n3. Identifying patients over 60 years old")
print(patients_df.loc[over_60_mask_np, ['patient_id', 'age']])

# ----------------------------------------------------------------
# 4. Calculate the correlation coefficient between age and
# treatment_duration using NumPy (excluding NULL values).
# ----------------------------------------------------------------
treatment_np = patients_df['treatment_duration'].to_numpy()

# Boolean mask: True where treatment_duration is not NaN
valid_treatment_mask = ~np.isnan(treatment_np)

# Apply mask to both arrays
age_clean_np = age_np[valid_treatment_mask]
treatment_clean_np = treatment_np[valid_treatment_mask]

# Calculate correlation coefficient
correlation_matrix = np.corrcoef(age_clean_np, treatment_clean_np)
correlation_coefficient = correlation_matrix[0, 1]

print("\n4. Correlation coefficient between age and treatment_duration\n")
print(correlation_coefficient)

# ----------------------------------------------------------------
#Part 2: Pandas Data Manipulation (40 points)
# ----------------------------------------------------------------
#5. Load both datasets into Pandas DataFrames.
# ----------------------------------------------------------------
# Display the first 5 rows and basic information
#(data types, non-null counts) for each DataFrame.
print("\nPart 2: Pandas Data Manipulation")

# Display the first 5 rows
print("\n5.Display the first 5 rows")
print("\nPatients:\n", patients_df.head())
print("\nTreatments:\n", outcomes_df.head())

# Display Dataframes info
print("\nDisplay Dataframe info")
print("\nPatients dataset info:")
patients_df.info()

print("\nTreatments dataset info:")
outcomes_df.info()

# ----------------------------------------------------------------
#6. Handle missing values:
# ----------------------------------------------------------------
#A. Identify how many NULL values exist in each DataFrame
# Count nulls
patients_null_counts = patients_df.isnull().sum()
outcomes_null_counts = outcomes_df.isnull().sum()

print("\n6A. Missing values")
print(f"\nPatients Dataframe:\n{patients_null_counts}")
print(f"\nTreatments Dataframe:\n{outcomes_null_counts}")

#B. Fill NULL values in 'treatment_duration' with the median duration for that diagnosis
median_duration_dict = {
    'Diabetes': patients_df.loc[patients_df['diagnosis'] == 'Diabetes', 'treatment_duration'].median(),
    'Hypertension': patients_df.loc[patients_df['diagnosis'] == 'Hypertension', 'treatment_duration'].median(),
    'Asthma': patients_df.loc[patients_df['diagnosis'] == 'Asthma', 'treatment_duration'].median()
}

# Apply medians only where treatment_duration is NaN
for diagnosis, median_value in median_duration_dict.items():
    patients_df.loc[ 
        (patients_df['diagnosis'] == diagnosis) & (
         patients_df['treatment_duration'].isna()),
         'treatment_duration'
    ] = median_value

print(f"\n6B. Fill NULL values with the median duration:\n{patients_df}")

#C. Drop rows with NULL blood pressure values in the Treatment Outcomes dataset
outcomes_df = outcomes_df.dropna(subset=['initial_blood_pressure', 'final_blood_pressure'])
print(f"\n6C. Drop rows with NULL blood pressure\n {outcomes_df}")

# ----------------------------------------------------------------
#7. Merge the two datasets on patient_id using an inner join.
# Display the resulting DataFrame.
# ----------------------------------------------------------------
merged_df = pd.merge(patients_df, outcomes_df, on='patient_id', how='inner')

#To display all the columns on the screen
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(f"\n7.Merge\n {merged_df}")


# ----------------------------------------------------------------
# Part 3: Introduction to scikit-learn (30 points)
# ----------------------------------------------------------------
# 8. Prepare the data for modeling:
# ----------------------------------------------------------------
# A. Create a feature matrix X with columns: age, treatment_duration,
# initial_blood_pressure, patient_satisfaction
# ----------------------------------------------------------------
# Remove rows where 'treatment_duration' is NULL before modeling
model_df = merged_df.dropna(
    subset=['treatment_duration']
)

# Create a feature matrix X
X = model_df[
    ['age', 'treatment_duration', 'initial_blood_pressure', 'patient_satisfaction']
]

print("\nPart 3: Introduction to scikit-learn")
print(f"\nFeature matrix X\n{X}")

# ----------------------------------------------------------------
# B. Create a target vector y with the readmission status
# (convert 'Yes'/'No' to 1/0)
# ----------------------------------------------------------------
y = model_df['readmission'].map({'Yes': 1, 'No': 0})

print(f"\nTarget vector y\n{y}")


# ----------------------------------------------------------------
# 9. Split the data into training (80%) and testing (20%) sets using
# train_test_split with random_state=42.
# ----------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining set shape:\n", X_train.shape)
print("\nTest set shape:\n", X_test.shape)

# ----------------------------------------------------------------
# 10. Apply StandardScaler from scikit-learn to normalize the features.
# Print the mean and standard deviation of each feature after scaling.
# ----------------------------------------------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nMean after scaling:", X_train_scaled.mean(axis=0))
print("\nStandard deviation after scaling:", X_train_scaled.std(axis=0))

# ----------------------------------------------------------------
# 11. Use scikit-learn's LogisticRegression to train a simple model
# predicting readmission. Report the accuracy score on the test set.
# ----------------------------------------------------------------
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print("\n\nAccuracy:", accuracy)







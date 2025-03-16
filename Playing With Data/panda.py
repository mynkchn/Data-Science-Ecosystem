import pandas as pd
import numpy as np

# ----------------- Data Creation -----------------
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

# ----------------- Data Exploration -----------------
print("Data Types:\n", df.dtypes, "\n")
print("Summary Statistics:\n", df.describe(), "\n")
print("First 2 rows:\n", df.head(2), "\n")  # Shows first 2 rows
print("Last 2 rows:\n", df.tail(2), "\n")    # Shows last 2 rows
print("Shape of DataFrame:", df.shape, "\n")   # (Rows, Columns)

# ----------------- Data Cleaning -----------------
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Filling missing values
df.drop_duplicates(inplace=True)  # Removing duplicate rows

# ----------------- Data Selection -----------------
print("Selecting a Single Column:\n", df['Name'], "\n")  # Single column
print("Selecting Multiple Columns:\n", df[['Name', 'Salary']], "\n")
print("Selecting Rows with loc:\n", df.loc[0:2], "\n")  # Select rows by label
print("Selecting Rows with iloc:\n", df.iloc[1:3], "\n")  # Select rows by index

# ----------------- Data Filtering -----------------
print("Filter: Salary > 60000:\n", df[df['Salary'] > 60000], "\n")
print("Filter: City == 'Delhi':\n", df[df['City'] == 'Delhi'], "\n")

# ----------------- Data Transformation -----------------
df['Bonus'] = df['Salary'] * 0.10  # Creating a new column
print("Data with Bonus Column:\n", df, "\n")

# ----------------- Data Grouping and Aggregation -----------------
print("Average Salary by City:\n", df.groupby('City')['Salary'].mean(), "\n")

# ----------------- Sorting -----------------
df_sorted = df.sort_values(by='Salary', ascending=False)
print("Sorted Data by Salary Descending:\n", df_sorted, "\n")

# ----------------- Merging DataFrames -----------------
data2 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Department': ['HR', 'Finance']
})
merged_df = pd.merge(df, data2, on='Name', how='left')
print("Merged DataFrame:\n", merged_df, "\n")

# ----------------- Pivot Table -----------------
pivot_df = df.pivot_table(values='Salary', index='City', aggfunc='mean')
print("Pivot Table:\n", pivot_df, "\n")

# ----------------- Exporting Data -----------------
df.to_csv('output.csv', index=False)  # Exporting as CSV file
print("Data exported successfully to 'output.csv'")

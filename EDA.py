# Exploratory Data Analysis (EDA)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/Users/mariecieslar/Desktop/Schreibtisch - Maries MacBook Air/Bocconi/Semester 1/STATS/Final Project/housing.csv'  # Replace with your file path
housing_data = pd.read_csv(file_path)

# 1. Dataset Overview
print("Dataset Overview:")
print(housing_data.info())  # Data types and non-null counts

# 2. Check for Missing Data
print("\nMissing Data:")
missing_data = housing_data.isnull().sum()
missing_percentage = (missing_data / len(housing_data)) * 100
missing_report = pd.DataFrame({'Missing Count': missing_data, 'Missing Percentage': missing_percentage})
print(missing_report[missing_report['Missing Count'] > 0].sort_values(by='Missing Percentage', ascending=False))

# Visualizing missing data as a heatmap (Optional)
plt.figure(figsize=(12, 8))
plt.imshow(housing_data.isnull(), aspect='auto', cmap='viridis', interpolation='nearest')
plt.colorbar(label='Missing Values (0=Not Missing, 1=Missing)')
plt.title('Heatmap of Missing Data')
plt.xlabel('Variables')
plt.ylabel('Observations')
plt.show()

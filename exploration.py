import pandas as pd

file_path = 'housing.csv'

data = pd.read_csv(file_path)

# Display basic information and the first few rows of the dataset for analysis.
data_info = data.info()
data_head = data.head()

# Adjust display options to show all columns
pd.set_option('display.max_columns', None)

data_description = data.describe(include='all')

print (f' data info:\n {data_info}, \n\n data_head:\n {data_head}, \n\n data_description:\n {data_description}')

# Print the count of missing values in each column
print('\n\n Missing data:', data.isnull().sum())
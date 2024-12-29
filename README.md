# stats-project
Stats girlies unite!

# notebooks and python files:

## cleaning_data.ipynb
for cleaning the missing values

What we have done:
- deleted column council area: not necessary for us, not many missing values, not a big loss to the database.
- detelet records with missing Car: again, not a big loss to the database.
- filled in values for yearbuilt and buildingarea
- (bonus: calculated correlation between building area and other values)

## adding_columns.ipynb
for feature engineering

What we have done:
- converted yearbuilt and propertycount into int
- converted date into datetime python format
- added dummies for regions
- added columns for building price per mq2, and land price per mq2
- (bonus: calculated correlation between the two above)

## eda_marie.ipynb
some starting eda

What we have done:
- First part:
  - price by regions (box plot)
  - regional avg price (hist)
  - geo map of property prices
  - geo map of property prices per sqm
- Second part
  - price per num of rooms (box plot)
  - price per num of bathrooms (box plot)
  - price per landsize (must fix)
  - Price by Distance from CBD (scatter plot)
  - Price, Distance from CBD, and Building Area (3d scatter plot, must fix)

## eda.py
to ignore

# datasets

## housing.csv
starting dataset

## cleaned_data.csv
dataset after running the cleaning_data.ipynb over housing.csv

## cleaned_and_complete_data.csv
dataset after running the adding_columns.ipynb over cleaned_Data.csv


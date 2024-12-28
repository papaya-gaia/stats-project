# My exploratory findings

Number of records: 13,580; number of attributes/columns: 21

- 8 columns with string data
- 13 columns with numerical data

Information about the columns:
- **Suburb**: Name of the suburb (314 unique).
- **Address**: Property address.
- **Rooms**: Number of rooms.
- **Type**: Property type (h: house, u: unit, t: townhouse).
- **Price**: Property price (from 85,000 to 9,000,000).
- **Method**: Sales method (S, SP, PI, etc.).
- **SellerG**: Seller's name.
- **Date**: Sale date.
- **Distance**: Distance from the city center (average: 10.- 14 km).
- **Postcode**: Postal code.
- **Bathroom**: Number of bathrooms (average: 1.53).
- **Car**: Number of parking spaces (average: 1.61).
- **Landsize**: Land size (average: 558.42 m², maximum: 433,- 014 m²).
- **BuildingArea**: Built area (available for 52.5% of the rows).
- **YearBuilt**: Year of construction (available for 60.4% of the rows).
- **CouncilArea**: Administrative area (33 unique).
- **Regionname**: Region (8 unique, e.g., Southern Metropolitan).
- **Lattitude** & **Longitude**
- **Propertycount**: Number of properties in the same 


## Missing values on:
Car, BuildingArea, YearBuilt, CouncilArea have missing values.

BuildingArea, YearBuilt have a loooot of missing values (around 47.5% and 39.6% of missing records)

In particular:
- **BuildingArea**:     6450
- **YearBuilt**:        5375
- **CouncilArea**:      1369
- **Car**:                62 (which may be related to the property type... as if a studio or a single unit might not even have the parking option normally. Just a speculation)


# data.describe()

|                  | Suburb       | Address        | Rooms         | Type | Price        | Method | SellerG | Date      | Distance     | Postcode    | Bedroom2     | Bathroom       | Car          | Landsize     | BuildingArea | YearBuilt   | CouncilArea  | Lattitude   | Longtitude   | Regionname             | Propertycount |
|------------------|--------------|----------------|---------------|------|--------------|--------|---------|-----------|--------------|-------------|--------------|----------------|--------------|--------------|--------------|-------------|--------------|-------------|--------------|------------------------|----------------|
| count            | 13580        | 13580          | 13580.000000  | 13580| 13580.000000 | 13580  | 13580   | 13580     | 13580.000000 | 13580.000000| 13580.000000 | 13580.000000   | 13518.000000 | 13580.000000 | 7130.000000  | 8205.000000 | 12211        | 13580.000000| 13580.000000 | 13580                  | 13580.000000   |
| unique           | 314          | 13378          | NaN           | 3    | NaN          | 5      | 268     | 58        | NaN          | NaN         | NaN          | NaN            | NaN          | NaN          | NaN          | NaN         | 33           | NaN         | NaN          | 8                      | NaN            |
| top              | Reservoir    | 5 Charles St   | NaN           | h    | NaN          | S      | Nelson  | 27/05/2017| NaN          | NaN         | NaN          | NaN            | NaN          | NaN          | NaN          | NaN         | Moreland     | NaN         | NaN          | Southern Metropolitan | NaN            |
| freq             | 359          | 3              | NaN           | 9449 | NaN          | 9022   | 1565    | 473       | NaN          | NaN         | NaN          | NaN            | NaN          | NaN          | NaN          | NaN         | 1163         | NaN         | NaN          | 4695                  | NaN            |
| mean             | NaN          | NaN            | 2.937997      | NaN  | 1075684.000  | NaN    | NaN     | NaN       | 10.137776    | 3105.301915 | 2.914728     | 1.534242       | 1.610075     | 558.416127   | 151.967650   | 1964.684217| NaN          | -37.809203  | 144.995216   | NaN                   | 7454.417378    |
| std              | NaN          | NaN            | 0.955748      | NaN  | 639310.700   | NaN    | NaN     | NaN       | 5.868725     | 90.676964   | 0.965921     | 0.691712       | 0.962634     | 3990.669241  | 541.014538   | 37.273762  | NaN          | 0.079260    | 0.103916     | NaN                   | 4378.581772    |
| min              | NaN          | NaN            | 1.000000      | NaN  | 85000.000    | NaN    | NaN     | NaN       | 0.000000     | 3000.000000 | 0.000000     | 0.000000       | 0.000000     | 0.000000     | 0.000000     | 1196.000000| NaN          | -38.182550  | 144.431810   | NaN                   | 249.000000     |
| 25%              | NaN          | NaN            | 2.000000      | NaN  | 650000.000   | NaN    | NaN     | NaN       | 6.100000     | 3044.000000 | 2.000000     | 1.000000       | 1.000000     | 177.000000   | 93.000000    | 1940.000000| NaN          | -37.856822  | 144.929600   | NaN                   | 4380.000000    |
| 50%              | NaN          | NaN            | 3.000000      | NaN  | 903000.000   | NaN    | NaN     | NaN       | 9.200000     | 3084.000000 | 3.000000     | 1.000000       | 2.000000     | 440.000000   | 126.000000   | 1970.000000| NaN          | -37.802355  | 145.000100   | NaN                   | 6555.000000    |
| 75%              | NaN          | NaN            | 3.000000      | NaN  | 1330000.000  | NaN    | NaN     | NaN       | 13.000000    | 3148.000000 | 3.000000     | 2.000000       | 2.000000     | 651.000000   | 174.000000   | 1999.000000| NaN          | -37.756400  | 145.058305   | NaN                   | 10331.000000   |
| max              | NaN          | NaN            | 10.000000     | NaN  | 9000000.000  | NaN    | NaN     | NaN       | 48.100000    | 3977.000000 | 20.000000    | 8.000000       | 10.000000    | 433014.000000| 44515.000000 | 2018.000000| NaN          | -37.408530  | 145.526350   | NaN                   | 21650.000000   |

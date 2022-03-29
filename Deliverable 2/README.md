# Manipulating Weather Data

## Raw Data

The raw weather data came from World Bank Group, Climate Change Knowledge Portal and was dowloaded for France, Italy, Spain and the US.  Observed, annual mean temperature and total precipitation as well as projected, annual mean temperature and total precipitation were downloaded.  

## Historical and Projected Data

Historical and projected precipitation and temperature were extracted from the country data for the following provinces/states:

- Alsace, France
- Aquitaine, France
- Burgundy, France
- Champagne Ardenne, France
- Piemonte, Italy
- Sardinia, Italy
- Sicily, Italy
- Tuscany, Italy
- Veneto, Italy
- Cantabria, Spain
- California, US
- New York, US
- Oregon, US
- Washington, US

Each download appeared like the following with data from 1901 - 2020 for the country as a whole and for each province.

![Example Download](https://github.com/mshideler/Group2/blob/mshideler/Deliverable%202/Resources/ExampleDownload.PNG)

Pandas was used to rearrange the data:

```
# Import dependency
import pandas as pd

# Read historic precipitation data in CSV to a DataFrame
file_path1 = "Spain Precipitation Historic.csv"
precip_df = pd.read_csv(file_path1)

# Rename unnamed column
precip_df = precip_df.rename(columns={'Unnamed: 0': 'Year'})

# Create new dataframe with applicable provinces
new_precip_df = precip_df[['Year', 'Cantabria']]

# Rename columns to ID them as precipitation columns
new_precip_df = new_precip_df.rename(columns={'Cantabria': 'Cantabria Precip'})

# Read historic temperature data in CSV to a DataFrame
file_path2 = "Spain Temp Historic.csv"
temp_df = pd.read_csv(file_path2)

# Rename unnamed column
temp_df = temp_df.rename(columns={'Unnamed: 0': 'Year'})

# Create new dataframe with applicable provinces
new_temp_df = temp_df[['Year', 'Cantabria']]

# Rename columns to ID them as temperature columns
new_temp_df = new_temp_df.rename(columns={'Cantabria': 'Cantabria Temp'})

# Merge the new_precip and new_temp DataFrames into one DataFrame
spain_df = pd.merge(new_precip_df, new_temp_df, on='Year')

# Add a column to specify which province the precipitation and temperature data is for
spain_df['Province'] = pd.Series(['Cantabria' for x in range(len(spain_df.index))])

# Rename the precipitation and temperature columns by replacing the province name with "Historical"
spain_df = spain_df.rename(columns={'Cantabria Precip': 'Historical Precip', 'Cantabria Temp': 'Historical Temp'})

# Reorder the columns
spain_df = spain_df[['Province', 'Year', 'Historical Precip', 'Historical Temp']]

# Save DataFrame to CSV
spain_df.to_csv('historical_weather_spain.csv', index=False)
```

And here is the resulting DataFrame that got saved as a CSV file:

![ExampleDF](https://github.com/mshideler/Group2/blob/mshideler/Deliverable%202/Resources/ExampleDF.PNG)

The above steps were performed for each province in a country to produce a Historical Data CSV and Projected Data CSV for each country.

## Combined Data

The historical CSV files and the projected CSV files were then combined using the following code:

```
# Import dependency
import pandas as pd

# Read historic weather data in CSVs to a DataFrame
# Declare empty DataFrame
historical_weather_df = pd.DataFrame()

file_paths = ("historical_weather_france.csv", "historical_weather_italy.csv", "historical_weather_spain.csv", "historical_weather_us.csv")

for path in file_paths:
    temp_df = pd.read_csv(path)
    historical_weather_df = pd.concat([historical_weather_df, temp_df])

# Save historical_weather_df to CSV
historical_weather_df.to_csv('historical_weather.csv', index=False)

# Read projected weather data in CSVs to a DataFrame
# Declare empty DataFrame
projected_weather_df = pd.DataFrame()

file_paths = ("projected_weather_france.csv", "projected_weather_italy.csv", "projected_weather_spain.csv", "projected_weather_us.csv")

for path in file_paths:
    temp_df = pd.read_csv(path)
    projected_weather_df = pd.concat([projected_weather_df, temp_df])

# Save projected_weather_df to CSV
projected_weather_df.to_csv('projected_weather.csv', index=False)

# Add "Timeseries" column to ID data in historical DF as Historical
historical_weather_df['Timeseries'] = pd.Series(['Historical' for x in range(len(historical_weather_df.index))])

# Rename Historical Precip and Historical Temp columns
historical_weather_df = historical_weather_df.rename(columns={'Historical Precip': 'Precipitation', 'Historical Temp': 'Temperature'})

# Add "Timeseries" column to ID data in projected DF as Projected
projected_weather_df['Timeseries'] = pd.Series(['Projected' for x in range(len(projected_weather_df.index))])

# Rename Projected Precip and Projected Temp columns
projected_weather_df = projected_weather_df.rename(columns={'Projected Precip': 'Precipitation', 'Projected Temp': 'Temperature'})

# Combine the historical data with the projected data
combined_weather_df = pd.concat([historical_weather_df, projected_weather_df])

# Additional edits after wine reviews EDA
# Remove Sardinia/Sardegna data
combined_weather_df = combined_weather_df[combined_weather_df.Province != 'Sardegna']

# Rename Toscana and Bourgogne so they match the corresponding province names in wine reviews
combined_weather_df.loc[combined_weather_df['Province']=='Toscana', 'Province']="Tuscany"
combined_weather_df.loc[combined_weather_df['Province']=='Bourgogne', 'Province']="Burgundy"

# Rename Province and Year for SQL join
combined_weather_df = combined_weather_df.rename(columns={'Province': 'Prov_Weather', 'Year': 'Year_Weather'})

# Save projected_weather_df to CSV
combined_weather_df.to_csv('combined_weather.csv', index=False)
```

This resulted in the creation of three CSV files containing only the combined historical data, only the combined projected data and then the combined historical and projected data resulting in an output similar to the following:

![Combined Weather Output](https://github.com/mshideler/Group2/blob/mshideler/Deliverable%202/Resources/WeatherOutputExample.png)

We anticipate using only the combined data in our analysis of wine quality; however, the other two files may be of use as well.  These files have been uploaded to a bucket at S3.


# Cleaning Wine Data

## Raw Data

The raw wine data, which contain over 80,000 wine reviews, came from Kaggle.    This dataset contains varieties of wine along with other information such where and when they came from, what wineries were used, how much they cost and what the review rating is.  The dataset initially looked like this:

![Raw Wine Data](https://github.com/mshideler/Group2/blob/mshideler/Deliverable%202/Resources/Raw_wine_data.PNG)

## Data Cleaning

The data cleaning for the wine reviews was minimal compared to what was needed for the weather data.  There is only one file to work with, so changes were made using Pandas in the following code:

```
# Import dependency
import pandas as pd

# Read in wine csv
wine_df = pd.read_csv("winedata.csv")
wine_df.head()

# Rename unnamed column
wine_df = wine_df.rename(columns={'Unnamed: 0': 'id'})

# Extract year column from title field, pop title
wine_df['year']=wine_df['title'].str.extract(r'([1-2]\d{3})')
wine_df.pop('title')

wine_df.head()

# Filter wine_df for regions we want to examine
regions=['California','Washington','Bordeaux','Tuscany','Oregon','Burgundy','Cantabria','Piedmont','Veneto','New York','Alsace','Sicily & Sardinia','Champagne']
wine_df_regions=wine_df[wine_df['province'].isin(regions)]
wine_df_regions

# Drop records with no year
wine_df_regions.dropna(subset=['year'],inplace=True)

# Drop records from before 1990
wine_df_regions=wine_df_regions[wine_df_regions['year']>'1990']

wine_df_regions

# Make list of columns to drop and drop them
columns_to_drop=['id','country','description','designation','price','region_2','region_1','winery']
wine_df_regions.drop(columns_to_drop,axis=1,inplace=True)

# Replace wine region values with matching regions from weather data
wine_df_regions.loc[wine_df_regions['province']=='Sicily & Sardinia','province']="Sicilia"
wine_df_regions.loc[wine_df_regions['province']=='Bordeaux','province']="Aquitaine"
wine_df_regions.loc[wine_df_regions['province']=='Northern Spain','province']="Cantabria"
wine_df_regions.loc[wine_df_regions['province']=='Champagne','province']="Champagne-Ardenne"
wine_df_regions.loc[wine_df_regions['province']=='Piedmont','province']="Piemonte"

# Reorder columns
wine_df_regions = wine_df_regions[['province', 'year', 'variety', 'points']]

wine_df_regions

# Save DataFrame to CSV
wine_df_regions.to_csv('cleaned_winereviews.csv', index=False)
```

## Resultant Wine Dataset

The final wine dataset appears as follows:

![Final Wine DF](https://github.com/mshideler/Group2/blob/mshideler/Deliverable%202/Resources/Final_wine_DF.PNG)

Like for the weather data, this DataFrame was exported to CSV and uploaded to AWS S3.

# Combined Weather and Wine Data

After using Google Colaboratory to write the weather and wine data to an Amazon RDS instance, we joined the data and created a new table using the following bit of SQL:

```
CREATE TABLE wine_weather_table
AS (SELECT * FROM wine_data 
	LEFT JOIN weather_data ON wine_data.province=weather_data.Prov_Weather AND wine_data.year=weather_data.Year_Weather
	WHERE weather_data.Timeseries = 'Historical');
```

Then, using SQLAlchemy and Pandas, we read wine_weather_table from SQL into a DataFrame in Pandas.

```
# Import dependencies
import pandas as pd
import psycopg2

import sqlalchemy
from sqlalchemy import create_engine

# Create an engine instance
alchemyEngine = create_engine('postgresql+psycopg2://root:Group2Wineos@grp2rdsinstance.cwkbfcctxu7y.us-east-1.rds.amazonaws.com/postgres')

# Connect to PostgreSQL server
dbConnection = alchemyEngine.connect();

df = pd.read_sql_table('wine_and_weather_table', dbConnection)
```

Here is the resulting output we'll use for our machine learning model:

![ML Dataset](https://github.com/mshideler/Group2/blob/mshideler/Deliverable%202/Resources/MLDataset.PNG)
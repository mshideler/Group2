# Group 2 Winos

# Topic
The topic of this project is predicting the quality of wine based on environmental factors such as geography, temperature and rainfall.  Climate change is expected to have a dramatic impact on these variables in the future and as enthusiastic wine drinkers, we hope to learn if this will have an impact on our preferred wine growing regions.  Specifically we hope to learn:

- Do higher temps and/or rainfall correlate with higher or lower quality wine?
- What affect will future changes in rainfall and temps have on wine quality from various regions?
- Are new regions poised to emerge as premiere locations for growing grapes and producing wine?

# Data Sources
### Environment Dataset
- https://climateknowledgeportal.worldbank.org/download-data
- The world bank provides observed rainfall and temperature data by year for regions within individual countries from 1901 to present.
- Future predictions of the with the same structure are provided which cover the years 2020-2100.
- The data has years in rows and regions in columns.

### Wine Reviews Dataset
- https://www.kaggle.com/zynicide/wine-reviews?select=winemag-data-130k-v2.csv
- This data set includes 130,000 records.
- Target variable is the 'points' field.
- Features include 'province', 'region', 'variety' and 'winery'.
- Includes reviews of wines from ~2000 to 2017.
- Will need to use RegEx to parse year from 'title' field.

### Regions to be examined:
- California, US
- Washington, US
- Bordeaux, France
- Tuscany, Italy
- Oregon, US
- Burgundy, France
- Cantabria, Spain  
- Piedmont, Italy   
- Veneto, Italy
- New York, US
- Alsace, France
- Sicily & Sardinia, Italy
- Champagne, France

# Communication Strategy

### Primary - Slack, Group2 Channel:
- The primary means of communication will be via the Group2 channel in Slack.

### Secondary - Email:
-Zack Gheen
zgheen88@gmail.com

-Kyle Johnson
kyle@ksjohnsons.com

-Marisa Shideler
marisa.shideler@outlook.com

-Brenya Skaggs
brenyask@gmail.com

### Meetings
- Meetings will be conducted on the zoom platform, when it is provided to us.
- Additional meeting will be held using Google Meet, which allows for a 60 minute meeting at no cost.

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
columns_to_drop=['id','country','description','designation','region_2','region_1','country']
wine_df_regions.drop(columns_to_drop,axis=1,inplace=True)

# Replace wine region values with matching regions from weather data
wine_df_regions.loc[wine_df_regions['province']=='Sicily & Sardinia','province']="Sicilia"
wine_df_regions.loc[wine_df_regions['province']=='Bordeaux','province']="Aquitaine"
wine_df_regions.loc[wine_df_regions['province']=='Northern Spain','province']="Cantabria"
wine_df_regions.loc[wine_df_regions['province']=='Champagne','province']="Champagne-Ardenne"
wine_df_regions.loc[wine_df_regions['province']=='Piedmont','province']="Piemonte"

# Drop rows where price is empty or less than 101
wine_df_regions=wine_df_regions.dropna(subset=['price'])
wine_df_regions=wine_df_regions[wine_df_regions['price']<101]

# Remove varieties with low counts
variety_counts=wine_df_regions.variety.value_counts()
replace_varieties=list(variety_counts[variety_counts<150].index)
replace_varieties

wine_df_regions=wine_df_regions[wine_df_regions['variety']!='NaN']
wine_df_regions

# Remove wineries with less than or equal to 3 occurrences
winery_vcs=wine_df_regions['winery'].value_counts()
winery_vcs

winery_counts=wine_df_regions.winery.value_counts()
replace_wineries=list(winery_counts[winery_counts<4].index)
len(replace_wineries)

wine_df_regions=wine_df_regions.groupby('winery').filter(lambda x: len(x)>3)

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


Overview of Group 2 Machine Learning Model
Overview
Our goal for this project has been to utilize Python libraries and machine learning techniques to manipulate and create a model on data to determine if there is a postive relationship between weather patterns and the quality of wine. We set out initially to determine if increasing global temperatures or changes in precipitation have had an effect on the quality of wine in regions renowned for their wine quality. Specifically we wanted to know if it was possible to predict if wine quality would increase or decrease in relation to these changes in the climate.

Data
The original two datasets we used were cleaned and formatted then imported into our PostGreSQL DB instance and joined in the database, we then exported this dataset back into the Model, and began steppping through the process of feature selection.

Multiple Linear Regression
We began the process with our library imports, creating a DB instance, and dropping any unnecessary or frivolous columns. We decided to drop all columns except points, price, province, variety, precipitation, and temperature.

image

We then encoded the columns of 'province', and 'variety' in order to get categorical values for these columns.

image

We then scaled the columns of 'precipitation', 'temperature', and 'price' using 'MinMaxScaler' from SKLearn, this ensured none of our variables showed inflated influence on the results of our model.

image

We then used 'points' column as our model's target and all othger columns as our variables.

image

image

We decided to first try using a Multiple Linear Regression model theorizing it may be a good fit since we wanted to determine the effectiveness of predicting continuous values over a period of time.

We used 'Train, Test, Split' and fit our model with 'X_train', and 'y_train'. We predicited using X_test. Our Mean_squared_error and R2_score came out as '5.7334', and '.33225' respectively

image

Due to the scores we tried to determine the importance of all our features, and found that features 53, 54, and 55 were our more important feratures so reran the model using only these three features.

Our mean_squared_error improved somewhat from 5.7334 to 6.17244, however our R_2 score decreased from .33225 to .28113.

Deep Learning
Due to the ineffectiveness of our Linear Regression Model we then tried our hand at using a Deep Learning Model. Our model set-up involved the three input features from second iteration of linear regression. We had two hidden layers with 20, and 15 nodes respectively. And we used 'Relu' and 'Sigmoid' activation functions

image

After compiling and fitting our model we ran it with 10 training epochs with the following results.

image

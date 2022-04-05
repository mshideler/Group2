# Winos

## Topic

The topic of this project is predicting the quality of wine based on environmental factors such as geography, temperature and rainfall. 
Climate change is expected to have a dramatic impact on these variables in the future and as enthusiastic wine drinkers, we hope to learn if 
this will have an impact on our preferred wine growing regions. Specifically we hope to learn:
* Do higher temps / rainfall correlate with higher or lower quality wine?
* What affect will future changes in rainfall and temps have on wine quality from various regions?
* Are new regions poised to emerge as premiere locations for growing grapes and prducing wine?


## Data Sources

###### Environment Dataset

* https://climateknowledgeportal.worldbank.org/download-data
* The world bank provides observed rainfall and temperature data by year for regions within individual countries from 1901 to present.
* Future predictions of the with the same structure are provided which cover the years 2020-2100.
* The data has years in rows and regions in columns

###### Wine Review Dataset

* https://www.kaggle.com/zynicide/wine-reviews?select=winemag-data-130k-v2.csv
* This dataset includes 130,000 records.
* Target variable is the *'points'* field. The features include *'province'*, *'region'*, *'variety'* and *'winery'*.
* Includes wine reviews from 2000-2017.

###### Regions to be examined:

* California, US
* Washington, US
* Aquitaine, France
* Tuscany, Italy
* Oregon, US
* Burgundy, France
* Cantabria, Spain
* Piemonte, Italy
* Veneto, ITaly
* New York, US
* Alsace, France
* Sardinia, Italy
* Champagne Ardenne, France
* Sicily, Italy


## Technologies, Language, Tools and Algorithms 


## Visualizations

###### Google Slides:
(URL)

###### Webpage:
(URL)



# Data Exploration Phase

## Manipulating Waether Data

## Raw Weather Data

he raw weather data came from World Bank Group, Climate Change Knowledge Portal and was dowloaded for France, Italy, Spain and the US. 
Observed, annual mean temperature and total precipitation as well as projected, annual mean temperature and total precipitation were downloaded.


## Historical and Projected Data

Historical and projected precipitation and temperature were extracted from the country data for the following provinces/states:

* California, US
* Washington, US
* Aquitaine, France
* Tuscany, Italy
* Oregon, US
* Burgundy, France
* Cantabria, Spain
* Piemonte, Italy
* Veneto, ITaly
* New York, US
* Alsace, France
* Sardinia, Italy
* Champagne Ardenne, France
* Sicily, Italy


Each download appeared like the following with data from 1901 - 2020 for the country as a whole and for each province.
(Image)

Pandas was used to rearrange the data:
(image)

And here is the resulting DataFrame that got saved as a CSV file:
(image)

The above steps were performed for each province in a country to produce a Historical Data CSV and Projected Data CSV for each country.


## Combined Data

The historical CSV files and the projected CSV files were then combined using the following code:
(image)

This resulted in the creation of three CSV files containing only the combined historical data, only the combined projected data 
and then the combined historical and projected data resulting in an output similar to the following:
(image)

We anticipate using only the combined data in our analysis of wine quality; however, the other two files may be of use as well. 
These files have been uploaded to a bucket at S3.




## Cleaning Wine Data

## Raw Wine Data

The raw wine data, which contain over 80,000 wine reviews, came from Kaggle. This dataset contains varieties of wine along with other information such where and when they came from, 
what wineries were used, how much they cost and what the review rating is. The dataset initially looked like this:
(image)

## Data Cleaning

The data cleaning for the wine reviews was minimal compared to what was needed for the weather data. There is only one file to work with, so changes were made using Pandas in the following code:
(image)


## Resultant Wine Dataset

The final wine dataset appears as follows:
(image)

Like for the weather data, this DataFrame was exported to CSV and uploaded to AWS S3. 


## Combined Weather and Wine Data

After using Google Colaboratory to write the weather and wine data to an Amazon RDS instance, we joined the data and created a new table using the following bit of SQL:
(imagE)

Then, using SQLAlchemy and Pandas, we read wine_weather_table from SQL into a DataFrame in Pandas.
(image)

Here is the resulting output we'll use for our machine learning model:
(image)




# Analysis Phase

## Machine Learning

###### Overview 

Our goal for this project has been to utilize Python libraries and machine learning techniques to manipulate and create a model on data to determine if there is a postive relationship between weather patterns and the quality of wine. 
We set out initially to determine if increasing global temperatures or changes in precipitation have had an effect on the quality of wine in regions renowned for their wine quality.
Specifically we wanted to know if it was possible to predict if wine quality would increase or decrease in relation to these changes in the climate.

###### Dataset

The original two datasets we used were cleaned and formatted then imported into our PostGreSQL DB instance and 
joined in the database, we then exported this dataset back into the Model, and began steppping through the process of feature selection.


## Multiple Linear Regression

We began the process with our library imports, creating a DB instance, and dropping any unnecessary or frivolous columns. 
We decided to drop all columns except points, price, province, variety, precipitation, and temperature.
(image)

We then encoded the columns of 'province', and 'variety' in order to get categorical values for these columns.
(image)
(image)

We then scaled the columns of 'precipitation', 'temperature', and 'price' using 'MinMaxScaler' from SKLearn, this ensured none of our variables showed inflated influence on the results of our model.
(image)

We them used 'points' column as our model's target and all other columns are our variables. 
(image)
(image)


###### M.L Obstacle

We decided to first try using a Multiple Linear Regression model theorizing it may be a good fit since we wanted to determine the effectiveness of predicting continuous values over a period of time.

We used 'Train, Test, Split' and fit our model with 'X_train', and 'y_train'. We predicited using X_test. Our Mean_squared_error and R2_score came out as '5.7334', and '.33225' respectively
(image)

Due to the scores we tried to determine the importance of all our features, and found that features 53, 54, and 55 were our more important feratures so reran the model using only these three features.

Our mean_squared_error improved somewhat from 5.7334 to 6.17244, however our R_2 score decreased from .33225 to .28113.

(image)


## Deep Learning

Due to the ineffectiveness of our Linear Regression Model we then tried our hand at using a Deep Learning Model. Our model set-up involved the three input features from second iteration of 
linear regression. We had two hidden layers with 20, and 15 nodes respectively. And we used 'Relu' and 'Sigmoid' activation functions
(image)

After compiling and fitting our model we ran it with 10 training epochs with the following results. 
(image)


## Summary



# **Winos**  :wine_glass:



## Overview of final project 

The topic of this project is predicting the quality of wine based on environmental factors such as geography, temperature and rainfall. Climate change is expected to have a dramatic impact on these variables in the future and as enthusiastic wine drinkers, we hope to learn if this will have an impact on our preferred wine growing regions. Specifically we hope to learn:


###### *Questions to Answer*

* Do higher temps / rainfall correlate with higher or lower quality wine?
* What affect will future changes in rainfall and temps have on wine quality from various regions?
* Are new regions poised to emerge as premiere locations for growing grapes and prducing wine?


## Data Source 
 
###### Environment Dataset

* https://climateknowledgeportal.worldbank.org/download-data
* The world bank provides observed rainfall and temperature data by year for regions within individual countries from 1901 to present.
* Future predictions of the with the same structure are provided which cover the years 2020-2100.


###### Wine Review Dataset

* https://www.kaggle.com/zynicide/wine-reviews?select=winemag-data-130k-v2.csv
* This dataset includes 130,000 records.
* Target variable is the *'points'* field. The features include *'province'*, *'region'*, *'variety'* and *'winery'*.




###### Regions to be examined:

* *California, US*

* *Washington, US*

* *Aquitaine, France*

* *Tuscany, Italy*

* *Oregon, US*

* *Burgundy, France*

* *Cantabria, Spain*

* *Piemonte, Italy*

* *Veneto, Italy*

* *New York, US*

* *Alsace, France*

* *Sardinia, Italy*

* *Cahmpagne Ardenne, France*

* *Sicily, Italy*

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/Map.png)






## Technologies, Language, Tools 

Python version 3.8.8
 - Tensor Flow
 - Pandas
 - Sklearn

AWS
 - RDS
 - S3

PostgreSQL/PGAdmin 

Flask

Google Colaboratory

Google Slides

Jupyter Notebook

HTML

CSS

Java Script

VSCode


## Google Slides  

[URL](https://docs.google.com/presentation/d/1nReyD5BZ179vePjs78I2nPNtlWJBdKqsc9oTfwqkcm8/edit?usp=sharing)


## Dashboard



## Machine Learning Flow Chart

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/Machine%20Learning%20Flow%20Chart.png)



# **Data Exploration** 

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Machine%20Learning/Updated_weatherdata_winedata_ERD.PNG)



## Weather Data
The raw weather data came from World Bank Group, Climate Change Knowledge Portal and was dowloaded for France, Italy, Spain and the US. Observed, annual mean temperature and total precipitation as well as projected, annual mean temperature and total precipitation were downloaded.


###### **Historical and Projected Data**


Historical and projected precipitation and temperature were extracted from the country data for the following provinces/states:

*California, US*
*Washington, US*
*Aquitaine, France*
*Tuscany, Italy*
*Oregon, US*
*Burgundy, France*
*Cantabria, Spain*
*Piemonte, Italy*
*Veneto, Italy*
*New York, US*
*Alsace, France*
*Sardinia, Italy*
*Cahmpagne Ardenne, France*
*Sicily, Italy*

Each download appeared like the following with data from 1901 - 2020 for the country as a whole and for each province.

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/ExampleDownload.PNG)

Pandas was used to rearrange the data to put in a form that we could easily join to the wine data.

Here is the resulting DataFrame that got saved as a CSV file:

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/ExampleDF.PNG)


This resulted in the creation of three CSV files containing only the combined historical data, only the combined projected data and then the combined historical and projected data resulting in an output similar to the following: 

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/WeatherOutputExample.png)

We used the historical combined data in our analysis of wine quality; however, the other two files may be of use as well. These files have been uploaded to a bucket at S3.




###### Wine Data

The raw wine data, which contain over 80,000 wine reviews, came from Kaggle. This dataset contains varieties of wine along with other information such where and when they came from, what wineries were used, how much they cost and what the review rating is. The dataset initially looked like this:

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/Raw_wine_data.PNG)

The data cleaning for the wine reviews was minimal compared to what was needed for the weather data. There is only one file to work with, so changes were made using Pandas. To complete this we had to filter the title and regions. Records prior to 1990 were dropped along with those without years. The regions were then renamed to match the weather data.

To help reduce noise we dropped rows where prices was empty or less than 101, we removed varities and wineries with low counts. 

The final wine dataset appears as follows:

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/Final_wine_DF.PNG)

Like for the weather data, this DataFrame was exported to CSV and uploaded to AWS S3.



# **Machine Learning** 


###### Overview

Our goal for this project has been to utilize Python libraries and machine learning techniques to manipulate and create a model on data to determine if there is a postive relationship between weather patterns and the quality of wine. We set out initially to determine if increasing global temperatures or changes in precipitation have had an effect on the quality of wine in regions renowned for their wine quality. Specifically we wanted to know if it was possible to predict if wine quality would increase or decrease in relation to these changes in the climate.

###### Dataset

The original two datasets we used were cleaned and formatted then imported into our PostGreSQL DB instance and joined in the database, we then exported this dataset back into the Model, and began steppping through the process of feature selection.


## Multiple Linear Regression

We began the process with our library imports, creating a DB instance, and dropping any unnecessary or frivolous columns. We decided to drop all columns except points, price, province, variety, precipitation, and temperature.

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/MLDataset.PNG)

We then encoded the columns of 'province', and 'variety' in order to get categorical values for these columns.

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/encode1.png)

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/encode2.png)

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/endf.png)

We then scaled the columns of *'precipitation'*, *'temperature'*, and *'price'* using 'MinMaxScaler' from SKLearn, this ensured none of our variables showed inflated influence on the results of our model.

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/mmsc.png)

We then used the 'points' column as our model's target and all other columns are our variables.

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/X.png)

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/y.png)



## **M.L. Obstacle** 

We decided to first try using a Multiple Linear Regression model theorizing it may be a good fit since we wanted to determine the effectiveness of predicting continuous values over a period of time.

We used 'Train, Test, Split' and fit our model with 'X_train', and 'y_train'. We predicited using X_test. Our Mean_squared_error and R2_score came out as '5.7334', and '.33225' respectively

Due to the scores we tried to determine the importance of all our features, and found that features 53, 54, and 55 were our more important feratures so reran the model using only these three features.

Our mean_squared_error improved somewhat from 5.7334 to 6.17244, however our R_2 score decreased from .33225 to .28113.

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/r2score.png)

## **Deep Learning** 

Due to the ineffectiveness of our Linear Regression Model we then tried our hand at using a Deep Learning Model. Our model set-up involved the three input features from second iteration of linear regression. We had two hidden layers with 20, and 15 nodes respectively. And we used 'Relu' and 'Sigmoid' activation functions 

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/DLMoutput.png)

After compiling and fitting our model we ran it with 10 training epochs with the following results. 

![This is an image](https://github.com/kylejohnsonks/Group2/blob/main/Resources/deep_learning_accuracy.png)



# **Results of Analysis** 

 Our initial machine learning analysis used a mmultiple linear regression model due to it's ability to predict a continuous variable, such as a wine's quality rating. This model produced a mean squared error and R-2 Score that we found unsuitable to produce a valid conclusion to our hypothesis. With this in mind we decided to try to find the feature importance of all our model's features, we found that the features **"precipitation_scaled, temperature_scaled, and price_scaled (53, 54, and 55)"** were our most influential features and thus re-ran our model with just these three features. This iteration of the linear regression model produced a better Mean Squared Error, but a worse R-2 score. with this in mind we decided to try a Deep Learning model which is also capable of predicting continuous varaibles and may give us a better accuracy score, we were wrong. Our accuracy score for this model choice was nearly an absolute zero, with loss numbers ranging from (-134513.7500, -154096944.0000). Ultimately we came to the conclusion that climate conditions in a wine growing region just are not accurate predictors of a wine's quality. However we have theorized that winery and price could be much better indicator of wine quality for the same reasons that climate is not a good indicator, well respected wine producers and growers know how to mitigate the effects of climate to produce better quality wines from their region. Additionally we thought it may be interesting to look at the variety of grapes grown in each region over time, to see if farmers are changing the variety of grapes they grow in response to climate changes.  






# **Overview of Group 2 Machine Learning Model**
--------------------------------------------

## **Overview**
---------------

Our goal for this project has been to utilize Python libraries and machine learning techniques to manipulate and create a model on data to determine if there is 
a postive relationship between weather patterns and the quality of wine. We set out initially to determine if increasing global temperatures or changes in precipitation have had an effect
on the quality of wine in regions renowned for their wine quality. Specifically we wanted to know if it was possible to predict if wine quality would increase or decrease in relation to these changes in the climate. 

## **Data** 
-----------

The original two datasets we used were cleaned and formatted then imported into our PostGreSQL DB instance and joined in the database, we then exported this dataset back into the Model,
 and began steppping through the process of feature selection.
 
 ## **Multiple Linear Regression**
 ---------------------------------------
 
We began the process with our library imports, creating a DB instance, and dropping any unnecessary or frivolous columns. We decided to drop all columns except points, price, province, variety, precipitation, and temperature.

![image](https://user-images.githubusercontent.com/93295751/161455751-9ca2b543-a666-487a-9edc-916410438bac.png)

We then encoded the columns of 'province', and 'variety' in order to get categorical values for these columns. 

![image](https://user-images.githubusercontent.com/93295751/161455828-09fab774-917b-49d9-aff2-74f2b94ed087.png)

We then scaled the columns of 'precipitation', 'temperature', and 'price' using 'MinMaxScaler' from SKLearn, this ensured none of our variables showed inflated influence on the results of our model. 

![image](https://user-images.githubusercontent.com/93295751/161455992-1f6bd266-b6e7-463a-a1a6-8a535047e3e5.png)

We then used 'points' column as our model's target and all othger columns as our variables. 

![image](https://user-images.githubusercontent.com/93295751/161456054-3424dd64-3788-41ef-b56d-f4e291b8a0b4.png)

![image](https://user-images.githubusercontent.com/93295751/161456068-cf578bd2-d60f-4107-b318-82365ae8dbf3.png)

We decided to first try using a Multiple Linear Regression model theorizing it may be a good fit since we wanted to 
determine the effectiveness of predicting continuous values over a period of time.

We used 'Train, Test, Split' and fit our model with 'X_train', and 'y_train'.
We predicited using X_test. Our Mean_squared_error and R2_score came out as '5.7334', and '.33225' respectively 

![image](https://user-images.githubusercontent.com/93295751/161456619-03f2b738-d115-4bce-b6a9-bfd117dfdd97.png)

Due to the scores we tried to determine the importance of all our features, and found that features 53, 54, and 55 were our
more important feratures so reran the model using only these three features. 
 
Our mean_squared_error improved somewhat from 5.7334 to 6.17244, however our R_2 score decreased from .33225 to .28113.

## **Deep Learning**

Due to the ineffectiveness of our Linear Regression Model we then tried our hand at using a Deep Learning Model. Our model set-up involved the three input features from
second iteration of linear regression. We had two hidden layers with 20, and 15 nodes respectively. And we used 'Relu' and 'Sigmoid' activation functions 

![image](https://user-images.githubusercontent.com/93295751/161457078-801c5a00-4042-4e6a-a728-23969447161a.png)

After compiling and fitting our model we ran it with 10 training epochs with the following results. 

![image](https://user-images.githubusercontent.com/93295751/161457149-57311d41-b91b-41ff-a9c6-5a038e542d14.png)


 



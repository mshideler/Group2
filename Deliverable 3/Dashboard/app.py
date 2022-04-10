
# Import dependencies
from unittest import result

from flask import Flask, render_template, redirect, session, jsonify
from joblib import load
import pandas as pd
#from sklearn.linear_model import LinearRegression


# Create a new Flask instance
app = Flask(__name__)


# Define the starting point or root
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/<province>/<variety>/<precipitation>/<temperature>/<price>')

def inputs(province,variety,precipitation,temperature,price):

    #province List
    provinces=['Alsace','Aquitaine','Burgundy','California','Champagne-Ardenne','New York','Oregon','Piemonte','Sicilia','Tuscany','Veneto','Washington']

    #variety list
    varieties=['Barbera','Bordeaux-style Red Blend','Bordeaux-style White Blend','Cabernet Franc','Cabernet Sauvignon','Champagne Blend','Chardonnay','Corvina','Dolcetto','Garganega','Gewurztraminer','Glera','Grenache','Malbec','Meritage','Merlot','Moscato','Mourvedre','Nebbiolo','Nero dAvola','Petit Verdot','Petite Sirah','Pinot Blanc','Pinot Grigio','Pinot Gris','Pinot Noir','Red Blend','Rhone-style Red Blend','Rhone-style White Blend','Riesling','Rose','Sangiovese','Sangiovese Grosso','Sauvignon Blanc','Sparkling Blend','Syrah','Tempranillo','Vermentino','Viognier','White Blend','Zinfandel']

    df_columns=provinces+varieties+['precipitation','temperature','price']

    #create dataframe with all zeros for captured values
    df=pd.DataFrame()
    for c in df_columns:
        df[c]=[0]

    #use province variable to set df[province]=1, same for variety, df[precip]=precip
    df[province]=1
    df[variety]=1
    df['precipitation']=precipitation
    df['temperature']=temperature
    df['price']=price

    #Load ML model
    model=load('Static/MLv4.joblib')
    
    #pass df to model for prediction
    result = model.predict(df)

    #return prediction to html    
    result2 = str(result)
    return jsonify(result2)

if __name__ == "__main__":
    app.run(debug=True)

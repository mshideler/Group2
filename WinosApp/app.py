
# Import dependencies
from unittest import result

from flask import Flask, render_template, redirect, session, jsonify
from joblib import load
import pandas as pd
from sklearn.linear_model import LinearRegression


# Create a new Flask instance
app = Flask(__name__,template_folder='Templates')


# Define the starting point or root
@app.route('/')
def index():
    return render_template("index.html")

#reset button function
@app.route('/reset')
def reset_page():
    return index()


#/predict/Oregon/Pinot Gris/14/8.68/440.1
@app.route('/predict/<province>/<variety>/<price>/<temperature>/<precipitation>')

def inputs(province,variety,price,temperature,precipitation):
    #create df to pass to scaler, add captured values
    scale_df=pd.DataFrame()
    scale_df['precipitation']=[precipitation]
    scale_df['temperature']=[temperature]
    scale_df['price']=[price]

    #load the saved scaler
    scaler=load('Static/js/Scaler_MLv4.joblib')

    #scale the df
    scaled_data=scaler.transform(scale_df)

    #province List
    provinces=['Alsace','Aquitaine','Burgundy','California','Champagne-Ardenne','New York','Oregon','Piemonte','Sicilia','Tuscany','Veneto','Washington']

    #variety list
    varieties=['Barbera','Bordeaux-style Red Blend','Bordeaux-style White Blend','Cabernet Franc','Cabernet Sauvignon','Champagne Blend','Chardonnay','Corvina','Dolcetto','Garganega','Gewurztraminer','Glera','Grenache','Malbec','Meritage','Merlot','Moscato','Mourvedre','Nebbiolo','Nero dAvola','Petit Verdot','Petite Sirah','Pinot Blanc','Pinot Grigio','Pinot Gris','Pinot Noir','Red Blend','Rhone-style Red Blend','Rhone-style White Blend','Riesling','Rose','Sangiovese','Sangiovese Grosso','Sauvignon Blanc','Sparkling Blend','Syrah','Tempranillo','Vermentino','Viognier','White Blend','Zinfandel']

    df_columns=provinces+varieties+['precipitation','temperature','price']

    #create dataframe with all zeros for captured values
    df=pd.DataFrame()
    for c in df_columns:
        df[c]=[0]

    #use province variable to set df[pr ovince]=1, same for variety, df[precip]=scaled data values
    df[province]=1
    df[variety]=1
    df['precipitation']=scaled_data[0][0]
    df['temperature']=scaled_data[0][1]
    df['price']=scaled_data[0][2]

    #Load ML model
    model=load('Static/js/MLv4.joblib')
        
    #pass df to model for prediction
    result = model.predict(df)

    #return prediction to html    
    result = str(int(round(result[0],0)))

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


# Import dependencies
from flask import Flask, render_template
from joblib import load
import pandas as pd
#import pandas as pd

# Create a new Flask instance
app = Flask(__name__)

#province List
provinces=['Oregon', 'Alsace', 'California', 'Sicilia', 'Aquitaine','Washington', 'Burgundy', 'New York', 'Tuscany', 'Piemonte','Veneto','Champagne-Ardenne']

#variety list
varieties=['Barbera','Bordeaux-style Red Blend','Bordeaux-style White Blend','Cabernet Franc','Cabernet Sauvignon','Champagne Blend','Chardonnay','Corvina','Dolcetto','Garganega','Gewurztraminer','Glera','Grenache','Malbec','Meritage','Merlot','Moscato','Mourvedre','Nebbiolo','Nero dAvola','Petit Verdot','Petite Sirah','Pinot Blanc','Pinot Grigio','Pinot Gris','Pinot Noir','Red Blend','Rhone-style Red Blend','Rhone-style White Blend','Riesling','Rose','Sangiovese','Sangiovese Grosso','Sauvignon Blanc','Sparkling Blend','Syrah','Tempranillo','Vermentino','Viognier','White Blend','Zinfandel']

df_columns=provinces+varieties+['precipitation','temperature','price']

# Define the starting point or root
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/<province>/<variety>/<precipitation>/<temperature>/<price>')
def inputs():
    #province List
    provinces=['Oregon', 'Alsace', 'California', 'Sicilia', 'Aquitaine','Washington', 'Burgundy', 'New York', 'Tuscany', 'Piemonte','Veneto','Champagne-Ardenne']

    #variety list
    varieties=['Barbera','Bordeaux-style Red Blend','Bordeaux-style White Blend','Cabernet Franc','Cabernet Sauvignon','Champagne Blend','Chardonnay','Corvina','Dolcetto','Garganega','Gewurztraminer','Glera','Grenache','Malbec','Meritage','Merlot','Moscato','Mourvedre','Nebbiolo','Nero dAvola','Petit Verdot','Petite Sirah','Pinot Blanc','Pinot Grigio','Pinot Gris','Pinot Noir','Red Blend','Rhone-style Red Blend','Rhone-style White Blend','Riesling','Rose','Sangiovese','Sangiovese Grosso','Sauvignon Blanc','Sparkling Blend','Syrah','Tempranillo','Vermentino','Viognier','White Blend','Zinfandel']

    df_columns=provinces+varieties+['precipitation','temperature','price']

    #create dataframe for captured values
    df=pd.DataFrame()
    for c in df_columns:
        df[c]=[0]

    #Load ML model
    model=load('Static/MLv4.joblib')
    return 'hi'

if __name__ == "__main__":
    app.run(debug=True)

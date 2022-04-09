
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

#Load ML model
model=load('Static/MLv4.joblib')

# Define the starting point or root
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def inputs():
    df=pd.DataFrame(data=[],columns=)
    return 'hi'

if __name__ == "__main__":
    app.run(debug=True)

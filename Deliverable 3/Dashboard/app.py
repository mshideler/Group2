
# Import dependencies
from flask import Flask, render_template
from joblib import load
#import pandas as pd

# Create a new Flask instance
app = Flask(__name__)

#Load ML model
model=load('Static/MLv4.joblib')

# Define the starting point or root
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def inputs():
    return 'hi'

if __name__ == "__main__":
    app.run(debug=True)

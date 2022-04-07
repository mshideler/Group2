
# Import dependencies
from flask import Flask, render_template
#import pandas as pd

# Create a new Flask instance
app = Flask(__name__)

# Define the starting point or root
@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/inputs')
#def inputs():
#    inputs = {"Temperature": a}
#    return a

if __name__ == "__main__":
    app.run(debug=True)

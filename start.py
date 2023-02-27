import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__, template_folder='template')
model = pickle.load(open('startup.pickle', 'rb'))


@app.route('/')
def home():
    return render_template('start.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('start.html',prediction_text="profit of the company is {}".format(math.floor(output)))
                           
if __name__ == '__main__':
    app.run(debug=True) 
                          
                           
                           
                           
                           
                           
                           
                           
                           




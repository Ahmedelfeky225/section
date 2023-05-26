import flask_restful
import joblib as joblib
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import joblib
import pandas as pd
from flask_cors import CORS

import sys
sys.modules['sklearn.externals.joblib'] = joblib


app = Flask(__name__)
CORS(app)

api = Api(app)

model = joblib.load(open('Coronav', 'rb'))


@app.route('/')
def home():
    return 'Corona result api 😧'


@app.route("/predictions", methods=['post'])
def predictions():
    results = request.json['results']
    predictions = model.predict([results, ])
    if predictions[0] == 0:
        return 'The person is Negative'
    else:
        return 'The person is positive '
    # return 'z' #jsonify(list(predictions))


if __name__ == '__main__':
    app.run(debug=True)

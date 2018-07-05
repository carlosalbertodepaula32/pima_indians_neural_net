from keras.models import load_model
import numpy as np
from flask import jsonify
import tensorflow as tf
from flask import Flask, request

app = Flask(__name__)

model = load_model('diabetes_model.h5')

global graph
graph = tf.get_default_graph()

@app.route("/diabetes/prediction")
def get_diabetes_prediction():
    with graph.as_default():
        pregnancies = request.args.get('pregnancies')
        plasmaGlucose = request.args.get('plasma_glucose')
        diastolicBloodPressure = request.args.get('diastolic_blood_pressure')
        tricepsThickness = request.args.get('triceps_thickness')
        serumInsulin = request.args.get('serum_insulin')
        age = request.args.get('age')

        data = np.matrix([[0, 1, 0, 1, 0, 0, 1, 1]])

        prediction =  model.predict(data)

        return jsonify(prediction.tolist())
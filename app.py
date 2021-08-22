import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from main import get_recommendations
import json
app = Flask(__name__)
model = pickle.load(open('movie.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    '''
  #  data = request.get_json
    print(request.args)
    data=request.args.get('movie')
    film=get_recommendations(data)
    print(film)
    result = film.to_json(orient="split")
    result2=json.loads(result)
    #return render_template('home.html', prediction_text='Movies are jkl')
    print(type(result))
    return render_template('home.html', prediction_text='Movies are {}'.format(result2['data']))


@app.route('/predict_api',methods=['POST','GET'])
def predict_api():

    data = request.get_json(force=True)
    film=get_recommendations(data['exp'])
    result = film.to_json(orient="split")
    return result


if __name__ == "__main__":
    app.run(debug=True)
from main import get_recommendations
import numpy as np
from flask import Flask, request, jsonify
import pickle as pkl


app = Flask(__name__)
with open('movie.pkl','rb') as f:
   cosine_sim=pkl.load(f)


@app.route('/api/',methods=['GET'])
def predict():
    data = request.get_json()
    film=get_recommendations(data['exp'])
    result = film.to_json(orient="split")
    return result

if __name__ == '__main__':
    app.run(port=5000, debug=True)

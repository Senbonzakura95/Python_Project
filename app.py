from flask import Flask, request, jsonify
from Python_Project.health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    bmi = calculate_bmi(height, weight)
    return jsonify({'bmi': bmi})

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    age = data['age']
    gender = data['gender']
    bmr = calculate_bmr(height, weight, age, gender)
    return jsonify({'bmr': bmr})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

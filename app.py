from flask import Flask, render_template, request
from predictor.py import predict_outcome

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    home_team = request.form['home_team']
    away_team = request.form['away_team']
    result = predict_outcome(home_team, away_team)
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)

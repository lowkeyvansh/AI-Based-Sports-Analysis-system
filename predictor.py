import joblib
import pandas as pd

def predict_outcome(home_team, away_team):
    model = joblib.load('soccer_model.pkl')

    # Preprocess the input
    le = LabelEncoder()
    df = pd.read_csv('soccer_matches.csv')
    le.fit(df['home_team'])
    home_team_encoded = le.transform([home_team])[0]
    away_team_encoded = le.transform([away_team])[0]

    X_new = [[home_team_encoded, away_team_encoded]]

    # Predict the outcome
    prediction = model.predict(X_new)[0]
    result = "Home Win" if prediction else "Away Win or Draw"
    return result

if __name__ == "__main__":
    result = predict_outcome('Manchester United', 'Chelsea')
    print(f'Predicted Outcome: {result}')

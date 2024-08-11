import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data():
    df = pd.read_csv('soccer_matches.csv')

    # Encode categorical variables
    le = LabelEncoder()
    df['home_team'] = le.fit_transform(df['home_team'])
    df['away_team'] = le.fit_transform(df['away_team'])

    # Define features and labels
    X = df[['home_team', 'away_team']]
    y = df['home_goals'] > df['away_goals']  # Label: 1 if home team wins, else 0

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    preprocess_data()

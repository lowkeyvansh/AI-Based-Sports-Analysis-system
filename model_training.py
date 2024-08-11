from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from data_preprocessing import preprocess_data
import joblib

def train_model():
    X_train, X_test, y_train, y_test = preprocess_data()

    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')

    # Save the trained model
    joblib.dump(model, 'soccer_model.pkl')

if __name__ == "__main__":
    train_model()

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load your dataset
df1 = pd.read_csv('diabetes.csv')

# ... (data preprocessing steps if needed)

# Model Building
X = df1.drop(columns='Outcome')
y = df1['Outcome']
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.20, random_state=0)

# Creating Random Forest Model
classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train, y_train)

# Saving the trained model to a pickle file
filename = 'diabetes-prediction-rfc-model.pkl'
try:
    with open(filename, 'wb') as file:
        pickle.dump(classifier, file)
        print(f"Model saved as {filename}")
except Exception as e:
    print(f"Error occurred while saving the model: {e}")

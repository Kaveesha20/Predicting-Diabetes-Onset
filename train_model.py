import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset (you'll need to download it from Kaggle)
# For now, we'll create a placeholder
try:
    diabetes_df = pd.read_csv('diabetes.csv')
except FileNotFoundError:
    print("Please download the diabetes.csv dataset from Kaggle and place it in the same directory")
    exit()

# Data preprocessing
diabetes_df_copy = diabetes_df.copy(deep=True)
diabetes_df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

# Fill missing values
diabetes_df_copy['Glucose'].fillna(diabetes_df_copy['Glucose'].mean(), inplace=True)
diabetes_df_copy['BloodPressure'].fillna(diabetes_df_copy['BloodPressure'].mean(), inplace=True)
diabetes_df_copy['SkinThickness'].fillna(diabetes_df_copy['SkinThickness'].median(), inplace=True)
diabetes_df_copy['Insulin'].fillna(diabetes_df_copy['Insulin'].median(), inplace=True)
diabetes_df_copy['BMI'].fillna(diabetes_df_copy['BMI'].median(), inplace=True)

# Feature scaling
sc_X = StandardScaler()
X = pd.DataFrame(sc_X.fit_transform(diabetes_df_copy.drop(["Outcome"],axis=1)), 
                 columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
y = diabetes_df_copy.Outcome

# Split the data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=42, stratify=y)

# Train Random Forest model
random_forest = RandomForestClassifier(random_state=42, n_estimators=100)
random_forest.fit(x_train, y_train)

# Save the model and scaler
joblib.dump(random_forest, 'random_forest_model.pkl')
joblib.dump(sc_X, 'scaler.pkl')

print("Model trained and saved successfully!")
print(f"Model accuracy: {random_forest.score(x_test, y_test):.2f}")
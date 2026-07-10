"""
Setup script for Diabetes Prediction App
This script will:
1. Download the dataset if not present
2. Train the model
3. Verify everything is ready
"""

import os
import urllib.request
import sys

def download_dataset():
    """Download the diabetes dataset if not present"""
    if os.path.exists('diabetes.csv'):
        print("✓ diabetes.csv already exists")
        return True
    
    print("Downloading diabetes dataset...")
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    
    try:
        urllib.request.urlretrieve(url, 'diabetes.csv')
        print("✓ Dataset downloaded successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to download dataset: {e}")
        print("\nPlease manually download from:")
        print("https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database")
        return False

def add_header_to_csv():
    """Add header row to the CSV if not present"""
    with open('diabetes.csv', 'r') as f:
        first_line = f.readline().strip()
    
    # Check if header already exists
    if 'Pregnancies' in first_line:
        print("✓ CSV header already present")
        return True
    
    # Add header
    print("Adding header to dataset...")
    header = "Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome\n"
    
    with open('diabetes.csv', 'r') as f:
        data = f.read()
    
    with open('diabetes.csv', 'w') as f:
        f.write(header)
        f.write(data)
    
    print("✓ Header added successfully")
    return True

def train_model():
    """Train the model"""
    print("\nTraining model...")
    print("This may take a minute...")
    
    try:
        import pandas as pd
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        import joblib
        
        # Load dataset
        diabetes_df = pd.read_csv('diabetes.csv')
        print(f"✓ Loaded {len(diabetes_df)} records")
        
        # Preprocess
        diabetes_df_copy = diabetes_df.copy(deep=True)
        diabetes_df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = \
            diabetes_df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0, np.NaN)
        
        # Fill missing values
        diabetes_df_copy['Glucose'].fillna(diabetes_df_copy['Glucose'].mean(), inplace=True)
        diabetes_df_copy['BloodPressure'].fillna(diabetes_df_copy['BloodPressure'].mean(), inplace=True)
        diabetes_df_copy['SkinThickness'].fillna(diabetes_df_copy['SkinThickness'].median(), inplace=True)
        diabetes_df_copy['Insulin'].fillna(diabetes_df_copy['Insulin'].median(), inplace=True)
        diabetes_df_copy['BMI'].fillna(diabetes_df_copy['BMI'].median(), inplace=True)
        
        # Feature scaling
        sc_X = StandardScaler()
        X = pd.DataFrame(sc_X.fit_transform(diabetes_df_copy.drop(["Outcome"], axis=1)), 
                         columns=['Pregnancies','Glucose','BloodPressure','SkinThickness',
                                 'Insulin','BMI','DiabetesPedigreeFunction','Age'])
        y = diabetes_df_copy.Outcome
        
        # Split data
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=1/3, 
                                                             random_state=42, stratify=y)
        
        # Train model
        print("Training Random Forest model...")
        random_forest = RandomForestClassifier(random_state=42, n_estimators=100)
        random_forest.fit(x_train, y_train)
        
        # Save model and scaler
        joblib.dump(random_forest, 'random_forest_model.pkl')
        joblib.dump(sc_X, 'scaler.pkl')
        
        accuracy = random_forest.score(x_test, y_test)
        print(f"✓ Model trained successfully!")
        print(f"✓ Model accuracy: {accuracy:.2%}")
        print(f"✓ Model saved to: random_forest_model.pkl")
        print(f"✓ Scaler saved to: scaler.pkl")
        
        return True
        
    except Exception as e:
        print(f"✗ Error training model: {e}")
        import traceback
        traceback.print_exc()
        return False

def verify_setup():
    """Verify all files are in place"""
    print("\nVerifying setup...")
    
    files = ['diabetes.csv', 'random_forest_model.pkl', 'scaler.pkl']
    all_present = True
    
    for file in files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} - MISSING")
            all_present = False
    
    return all_present

def main():
    print("=" * 60)
    print("Diabetes Prediction App - Setup")
    print("=" * 60)
    
    # Step 1: Download dataset
    if not download_dataset():
        print("\nSetup failed. Please download the dataset manually.")
        sys.exit(1)
    
    # Step 2: Add header if needed
    if not add_header_to_csv():
        print("\nSetup failed.")
        sys.exit(1)
    
    # Step 3: Train model
    if not train_model():
        print("\nSetup failed.")
        sys.exit(1)
    
    # Step 4: Verify
    if verify_setup():
        print("\n" + "=" * 60)
        print("✓ Setup complete! All files ready.")
        print("=" * 60)
        print("\nTo run the application:")
        print("  python app.py")
        print("\nThen open your browser to: http://localhost:5000")
    else:
        print("\n✗ Setup incomplete. Some files are missing.")
        sys.exit(1)

if __name__ == '__main__':
    main()
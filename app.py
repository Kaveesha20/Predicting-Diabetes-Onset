from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and scaler
try:
    model = joblib.load('random_forest_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("Model and scaler loaded successfully!")
except FileNotFoundError:
    print("Warning: Model files not found. Please run train_model.py first.")
    model = None
    scaler = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded. Please run train_model.py first to train the model.'}), 500
    
    try:
        # Get data from the form
        data = {
            'Pregnancies': float(request.form['pregnancies']),
            'Glucose': float(request.form['glucose']),
            'BloodPressure': float(request.form['blood_pressure']),
            'SkinThickness': float(request.form['skin_thickness']),
            'Insulin': float(request.form['insulin']),
            'BMI': float(request.form['bmi']),
            'DiabetesPedigreeFunction': float(request.form['diabetes_pedigree']),
            'Age': float(request.form['age'])
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([data])
        
        # Scale the input
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        
        # Return result
        result = {
            'prediction': int(prediction),
            'probability': float(probability),
            'risk_level': 'High' if probability > 0.5 else 'Low'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
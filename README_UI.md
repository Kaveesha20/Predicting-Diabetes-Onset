# Diabetes Prediction App - UI Guide

This guide explains how to use the web-based UI for the diabetes prediction model.

## 📋 Prerequisites

- Python 3.7 or higher
- pip package manager
- The diabetes dataset (`diabetes.csv`) from [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download the Dataset

Download the `diabetes.csv` file from the [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) and place it in the project root directory.

### 3. Train the Model

Run the training script to train the Random Forest model and save it:

```bash
python train_model.py
```

This will create two files:
- `random_forest_model.pkl` - The trained model
- `scaler.pkl` - The feature scaler

### 4. Run the Application

Start the Flask web server:

```bash
python app.py
```

The application will be available at: `http://localhost:5000`

## 📱 Using the Application

1. **Open your browser** and navigate to `http://localhost:5000`

2. **Enter patient information** in the form fields:
   - **Patient Information:**
     - Pregnancies: Number of pregnancies
     - Glucose: Plasma glucose concentration (mg/dL)
     - Blood Pressure: Diastolic blood pressure (mm Hg)
     - Skin Thickness: Triceps skinfold thickness (mm)
   
   - **Additional Measurements:**
     - Insulin: 2-hour serum insulin (mu U/ml)
     - BMI: Body mass index (kg/m²)
     - Diabetes Pedigree Function: Genetic risk factor
     - Age: Age in years

3. **Click the "Predict Diabetes Risk" button**

4. **View the results:**
   - Risk level (High/Low)
   - Probability percentage
   - Input summary for verification

## 🛠️ Project Structure

```
Predicting-Diabetes-Onset/
├── app.py                      # Flask backend server
├── train_model.py              # Model training script
├── requirements.txt            # Python dependencies
├── diabetes.csv               # Dataset (download from Kaggle)
├── random_forest_model.pkl    # Trained model (generated)
├── scaler.pkl                 # Feature scaler (generated)
├── templates/
│   └── index.html             # Frontend UI
├── Predict_Diabetes.ipynb     # Original Jupyter notebook
└── README.md                  # Project documentation
```

## 🔧 Troubleshooting

### Model files not found
If you see "Model not found" error:
1. Ensure you have `diabetes.csv` in the project directory
2. Run `python train_model.py` to train and save the model

### Port already in use
If port 5000 is already in use, you can change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to any available port
```

### Module not found errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## 🎨 Features

- **Modern, responsive design** with gradient backgrounds
- **Real-time predictions** with loading animation
- **Color-coded results** (red for high risk, green for low risk)
- **Detailed input summary** for verification
- **Medical disclaimer** for responsible use
- **Mobile-friendly** responsive layout
- **Smooth animations** and transitions

## ⚠️ Medical Disclaimer

This application is for **educational purposes only**. The predictions should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider.

## 📊 Model Information

- **Algorithm:** Random Forest Classifier
- **Dataset:** Pima Indians Diabetes Dataset
- **Features:** 8 clinical parameters
- **Performance:** ~77-82% accuracy

## 🔄 API Endpoint

The application also provides a REST API endpoint:

**POST** `/predict`

**Request Body (form-data):**
- `pregnancies`: Number
- `glucose`: Number
- `blood_pressure`: Number
- `skin_thickness`: Number
- `insulin`: Number
- `bmi`: Number
- `diabetes_pedigree`: Number
- `age`: Number

**Response:**
```json
{
  "prediction": 0 or 1,
  "probability": 0.1234,
  "risk_level": "Low" or "High"
}
```

## 📝 Example Usage

```bash
# Train the model
python train_model.py

# Run the web app
python app.py

# Open browser to http://localhost:5000
```

## 🤝 Contributing

Feel free to enhance the UI or improve the model integration. Some ideas:
- Add more visualization charts
- Implement model comparison (Logistic Regression vs Random Forest)
- Add patient history tracking
- Export predictions to PDF
- Add user authentication for medical professionals
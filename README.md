# Predicting Diabetes Onset

This project predicts the likelihood of diabetes onset using machine learning algorithms, including **Logistic Regression** and **Random Forest**, based on the **Pima Indians Diabetes Dataset**.

## 📊 Dataset
The dataset contains 768 records with features such as:
- Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age.
- The target variable is binary: 1 = diabetes, 0 = no diabetes.

## 🛠️ Technologies Used
- **Python**
- **Machine Learning Models**:
 **Logistic Regression**: A simple, interpretable model
 **Random Forest**: An ensemble method that improves prediction accuracy
- 
- **Libraries**: pandas, scikit-learn, matplotlib, numpy
- -**Google Colab**
  
- **Data Preprocessing**: Handling missing values, outlier detection, feature scaling
**Exploratory Data Analysis**: Visualizations using seaborn and matplotlib
  
  ## Results & Evaluation

- **Logistic Regression** achieved an **AUC score of 0.8245**.
- **Random Forest** performed slightly better with an **AUC score of 0.8204**.
- **Random Forest** showed **higher predictive accuracy and robustness**, making it preferable for deployment.
- **Future Work**:
  - Implement **ensemble methods** to further improve model performance.
  - Handle **class imbalance** using **SMOTE (Synthetic Minority Over-sampling Technique)**.

**References**  
Pima Indians Diabetes Dataset - Kaggle  
Scikit-Learn Documentation  

## 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Kaveesha20/Predicting-Diabetes-Onset.git
2. Run the Jupyter notebook or Python script to train and evaluate the models. 

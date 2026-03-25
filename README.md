# Student Study Recommendation System

## Overview
This project is a simple machine learning-based system that analyzes a student's study habits and provides personalized study recommendations.

It predicts the performance level (Low / Average / Good) based on factors like study hours, concentration, distractions, and sleep, and then suggests improvements.

---

## Technologies Used
- Python  
- Pandas  
- Scikit-learn (Logistic Regression)

---

## How It Works
- The model is trained on a dataset of student habits  
- User inputs are taken through the console  
- The model predicts performance level  
- Based on the prediction, recommendations and basic analysis are shown  

---

## Input Features
- Study Hours  
- Concentration Level (1–10)  
- Distraction Level (1–10)  
- Sleep Hours  

---

## Output
- Predicted Performance Level (Low / Average / Good)  
- Basic analysis (e.g., high distraction, low study time)  
- Study recommendations  

---

## How to Run
```bash
pip install pandas scikit-learn
python main.py

import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("data.csv")

# Features (inputs)
X = data[["study_hours", "concentration", "distraction", "sleep_hours"]]

# Target (output)
y = data["performance"]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Take user input
study_hours = float(input("Enter study hours: "))
concentration = float(input("Enter concentration level (1-10): "))
distraction = float(input("Enter distraction level (1-10): "))
sleep_hours = float(input("Enter sleep hours: "))

# Predict performance
prediction = model.predict([[study_hours, concentration, distraction, sleep_hours]])

# Recommendation logic
if prediction[0] == 0:
    print("Low performance: Reduce distractions and increase study time.")
elif prediction[0] == 1:
    print("Average performance: Improve consistency and focus.")
else:
    print("Good performance: Keep maintaining your current routine!")

import pandas as pd
from sklearn.linear_model import LogisticRegression

# loading the dataset
data = pd.read_csv("data.csv")

# selecting input features
features = data[["study_hours", "concentration", "distraction", "sleep_hours"]]

# target variable (what we want to predict)
target = data["performance"]

# creating and training the model
model = LogisticRegression()
model.fit(features, target)

print("\n--- Student Study Recommendation System ---\n")

# taking user input
study = float(input("Enter your daily study hours: "))
focus = float(input("Enter your concentration level (1-10): "))
distraction = float(input("Enter your distraction level (1-10): "))
sleep = float(input("Enter your sleep hours: "))

# making prediction
result = model.predict([[study, focus, distraction, sleep]])

# giving recommendation based on result
if result[0] == 0:
    print("\n⚠️ Your performance is likely LOW.")
    print("Try increasing study time and reducing distractions.\n")

elif result[0] == 1:
    print("\n⚡ Your performance is AVERAGE.")
    print("Work on consistency and improving focus.\n")

else:
    print("\n✅ Your performance is GOOD.")
    print("Keep maintaining your current routine!\n")

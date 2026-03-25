import pandas as pd
from sklearn.linear_model import LogisticRegression

# loading the dataset
data = pd.read_csv("data.csv")

# selecting input features
features = data[["study_hours", "concentration", "distraction", "sleep_hours"]]

# target variable
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

# converting numeric result to label
if result[0] == 0:
    level = "LOW"
elif result[0] == 1:
    level = "AVERAGE"
else:
    level = "GOOD"

print(f"\n📊 Predicted Performance Level: {level}")

# basic analysis (this makes it feel smarter)
print("\n🔍 Analysis:")
if distraction > 6:
    print("- High distraction detected")
if study < 4:
    print("- Low study time")
if sleep < 6:
    print("- Insufficient sleep")
if focus < 5:
    print("- Low concentration")

# recommendation
print("\n💡 Recommendation:")
if result[0] == 0:
    print("You should reduce distractions and increase focused study time.")
elif result[0] == 1:
    print("Try to improve consistency and manage distractions better.")
else:
    print("You're doing well. Maintain your current routine!")


# Import the CSV module to read data
import csv

# 1️⃣ Make sure to download the dataset from Kaggle:
# https://www.kaggle.com/datasets/arashnic/fitbit
# Extract the file and place the 'fitness_tracker_data.csv' in the same folder as this script

# 2️⃣ You can run this Python script using any Python IDE or simply with:
# python fitness-data-analyzer.py

# Question 1: How many users burned more than 2500 calories in a day?
with open("fitness_tracker_data.csv") as file:
    reader = csv.DictReader(file)
    high_calorie_burners = [row for row in reader if float(row["Calories"]) > 2500]
    print("Number of users who burned more than 2500 calories:", len(high_calorie_burners))

# Question 2: List all users who walked more than 10,000 steps in a day
with open("fitness_tracker_data.csv") as file:
    reader = csv.DictReader(file)
    print("\nUsers who walked more than 10,000 steps:")
    for row in reader:
        if int(row["TotalSteps"]) > 10000:
            print("User ID:", row["Id"], "- Steps:", row["TotalSteps"])

# Question 3: Print average hours of sleep for users aged between 25 and 40
# Note: We assume there is an 'Age' column in the dataset (some fitness datasets have it, or you can add it)
# For the sake of example, let's assume such column exists.

with open("fitness_tracker_data.csv") as file:
    reader = csv.DictReader(file)
    sleep_hours = []
    for row in reader:
        try:
            age = int(row["Age"])
            if 25 <= age <= 40:
                sleep_hours.append(float(row["TotalMinutesAsleep"]) / 60)  # convert to hours
        except:
            continue

    if sleep_hours:
        avg_sleep = sum(sleep_hours) / len(sleep_hours)
        print("\nAverage sleep (hours) for users aged 25-40:", round(avg_sleep, 2))
    else:
        print("\nNo sleep data found for users aged 25-40.")

# Step 1: Set up the environment
# Step 2: Create a dataset
monthly_rainfall = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Rainfall (mm)": [78, 50, 100, 130, 150, 200, 220, 210, 180, 140, 90, 80]
}

# Step 3: Load the data into a DataFrame
import pandas as pd

df = pd.DataFrame(monthly_rainfall)

# Display the DataFrame
print("Monthly Rainfall DataFrame:")
print(df)

# Step 4: Calculate the average rainfall
average_rainfall = df["Rainfall (mm)"].mean()
print(f"\nAverage Monthly Rainfall: {average_rainfall} mm")

# Step 5: Visualize the data
import matplotlib.pyplot as plt

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Month"], df["Rainfall (mm)"], color='skyblue')
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall")
plt.axhline(y=average_rainfall, color='r', linestyle='--', label=f'Average Rainfall: {average_rainfall} mm')
plt.xticks(rotation=45)
plt.legend()
plt.show()

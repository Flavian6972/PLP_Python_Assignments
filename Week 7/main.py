import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Load and Explore Dataset
try:
    # Sample sales dataset
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Coffee_Sales': [120, 150, 170, 160, 180],
        'IceCream_Sales': [80, 100, 90, 110, 130],
        'Region': ['North', 'South', 'East', 'West', 'North']
    }
    df = pd.DataFrame(data)
    
    print("First 5 rows:")
    print(df.head())
    print("\nData Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
except FileNotFoundError:
    print("Dataset not found.")

# Task 2: Basic Analysis
print("\nBasic Statistics:")
print(df.describe())

print("\nAverage Coffee Sales by Region:")
print(df.groupby('Region')['Coffee_Sales'].mean())

# Task 3: Visualizations

# Line Chart
plt.plot(df['Month'], df['Coffee_Sales'], marker='o', label='Coffee')
plt.plot(df['Month'], df['IceCream_Sales'], marker='o', label='Ice Cream')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Bar Chart
avg_sales = df.groupby('Region')['Coffee_Sales'].mean()
avg_sales.plot(kind='bar')
plt.title("Average Coffee Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Sales")
plt.show()

# Histogram
plt.hist(df['IceCream_Sales'], bins=5, color='orange')
plt.title("Distribution of Ice Cream Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.scatter(df['Coffee_Sales'], df['IceCream_Sales'], color='green')
plt.title("Coffee vs Ice Cream Sales")
plt.xlabel("Coffee Sales")
plt.ylabel("Ice Cream Sales")
plt.show()

# Observations
print("\nObservations:")
print("- Coffee sales increased steadily over months.")
print("- Ice cream sales also grew but with more variation.")
print("- North region had relatively higher coffee sales on average.")

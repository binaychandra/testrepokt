import pandas as pd
# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Score': [88, 92, 95, 85]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Simple processing: calculate mean age and mean score
mean_age = df['Age'].mean()
mean_score = df['Score'].mean()

print("Sample Data:")
print(df)
print(f"\nMean Age: {mean_age}")
print(f"Mean Score: {mean_score}")
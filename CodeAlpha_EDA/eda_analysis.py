import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("E:\\CodeAlpha_Internship\\CodeAlpha_EDA\\netflix_titles.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Count Movies vs TV Shows
print("\nType Counts:")
print(df['type'].value_counts())

# Visualization
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.show()
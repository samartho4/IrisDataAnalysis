
import pandas as pd

# Reading the CSV file
df = pd.read_csv("Iris.csv")

# Printing top 5 rows
print(df.head())

# Getting the shape of the dataset
print(df.shape)

# Getting info about the dataset
print(df.info())

# Statistical summary
print(df.describe())

# Checking for missing values
print(df.isnull().sum())

# Checking for duplicates
data = df.drop_duplicates(subset="Species")
print(data)

# Checking value counts for species
print(df['Species'].value_counts())

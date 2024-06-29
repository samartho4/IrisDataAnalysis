# iris_correlation_outliers.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Reading the CSV file
df = pd.read_csv("Iris.csv")

# Exclude the 'Species' column for correlation matrix
correlation_matrix = df.drop(columns=["Species"]).corr(method='pearson')
print(correlation_matrix)

# Heatmap of the correlation matrix
sns.heatmap(correlation_matrix, annot=True)
plt.show()

# Boxplot for each feature by species
def graph(y):
    sns.boxplot(x="Species", y=y, data=df)

plt.figure(figsize=(10, 10))

plt.subplot(221)
graph('SepalLengthCm')

plt.subplot(222)
graph('SepalWidthCm')

plt.subplot(223)
graph('PetalLengthCm')

plt.subplot(224)
graph('PetalWidthCm')

plt.show()

# Detecting and removing outliers using IQR for 'SepalWidthCm'
Q1 = np.percentile(df['SepalWidthCm'], 25, interpolation='midpoint')
Q3 = np.percentile(df['SepalWidthCm'], 75, interpolation='midpoint')
IQR = Q3 - Q1

print("Old Shape: ", df.shape)

# Upper bound
upper = np.where(df['SepalWidthCm'] >= (Q3 + 1.5 * IQR))

# Lower bound
lower = np.where(df['SepalWidthCm'] <= (Q1 - 1.5 * IQR))

# Removing the outliers
df.drop(upper[0], inplace=True)
df.drop(lower[0], inplace=True)

print("New Shape: ", df.shape)

sns.boxplot(x='SepalWidthCm', data=df)
plt.show()

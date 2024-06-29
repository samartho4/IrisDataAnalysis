
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Reading the CSV file
df = pd.read_csv("Iris.csv")

# Countplot for species
sns.countplot(x='Species', data=df)
plt.show()

# Scatterplot: Sepal Length vs Sepal Width
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

# Scatterplot: Petal Length vs Petal Width
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

# Pairplot for all relationships
sns.pairplot(df.drop(['Id'], axis=1), hue='Species', height=2)
plt.show()

# Histograms for each feature
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].set_title("Sepal Length")
axes[0, 0].hist(df['SepalLengthCm'], bins=7)

axes[0, 1].set_title("Sepal Width")
axes[0, 1].hist(df['SepalWidthCm'], bins=5)

axes[1, 0].set_title("Petal Length")
axes[1, 0].hist(df['PetalLengthCm'], bins=6)

axes[1, 1].set_title("Petal Width")
axes[1, 1].hist(df['PetalWidthCm'], bins=6)

plt.show()

# Distplot for each feature by species
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "SepalLengthCm").add_legend()
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "SepalWidthCm").add_legend()
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "PetalLengthCm").add_legend()
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "PetalWidthCm").add_legend()
plt.show()

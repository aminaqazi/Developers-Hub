import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('Iris.csv')

# Set style
sns.set_theme(style="whitegrid")

# --- 1. Scatter Plot ---
plt.figure(figsize=(8, 4))
sns.scatterplot(data=df, x='SepalLengthCm', y='SepalWidthCm', hue='Species')
plt.title('Sepal Length vs Width')
plt.savefig('scatter_plot.png')  # SAVE FIRST
print("Saved scatter_plot.png")
plt.show()                       # SHOW SECOND

# --- 2. Histograms ---
# We use plt.clf() to clear the previous figure so they don't overlap
plt.clf() 
df.drop('Id', axis=1).hist(edgecolor='black', figsize=(10, 8))
plt.suptitle('Value Distributions')
plt.savefig('histograms.png')    # SAVE FIRST
print("Saved histograms.png")
plt.show()

# --- 3. Box Plot ---
plt.figure(figsize=(8, 4))
sns.boxplot(x='Species', y='PetalLengthCm', data=df)
plt.title('Petal Length by Species')
plt.savefig('box_plot.png')      # SAVE FIRST
print("Saved box_plot.png")
plt.show()
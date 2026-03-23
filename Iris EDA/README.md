# Task 1: Iris Dataset Exploration & Visualization

## 🎯 Objective
The goal of this project is to load, inspect, and visualize the classic Iris dataset to understand data trends, feature distributions, and identify potential outliers using Python.

## 📊 Dataset
The **Iris Flower Dataset** (`Iris.csv`) contains 150 observations of iris flowers with the following features:
* **Features:** SepalLengthCm, SepalWidthCm, PetalLengthCm, and PetalWidthCm.
* **Target:** Three species of Iris (*Iris-setosa*, *Iris-versicolor*, and *Iris-virginica*).

## 🛠️ Tools & Libraries Used
* **Python:** Core programming language.
* **Pandas:** Data manipulation and inspection.
* **Matplotlib & Seaborn:** Data visualization and statistical plotting.
* **VS Code:** Integrated Development Environment (IDE).

## 🔍 Key Findings & Results
After exploring the data, here are the primary observations:
1. **Species Separation:** The *Setosa* species is clearly separated from the other two species, especially in petal measurements.
2. **Correlations:** There is a strong positive correlation between petal length and petal width.
3. **Outliers:** The **Box Plot** revealed that *Iris-setosa* has a few outliers in the **SepalWidthCm** feature.
4. **Saved Visuals:** This project generates and saves three visual reports:
   * `scatter_plot.png` (Feature relationships)
   * `histograms.png` (Data distributions)
   * `box_plot.png` (Outlier detection)

## 🚀 How to Run
1. **Clone the repository** to your local machine.
2. **Install Dependencies**:
   ```bash
   pip install pandas seaborn matplotlib
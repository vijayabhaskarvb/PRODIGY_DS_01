import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings

# Ignore warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the dataset
dataset = pd.read_csv('dataset.csv')

# Group by continent and sum population
continent_population = dataset.groupby("continent")["2022 population"].sum().sort_values()

# Bar chart for continent-wise population
def plot_bar_chart():
    plt.figure(figsize=(10, 6))
    sns.barplot(x=continent_population.values, y=continent_population.index, hue=continent_population.index, palette="viridis", legend=False)
    plt.xlabel("Total Population (2022)")
    plt.ylabel("Continent")
    plt.title("Population Distribution by Continent (2022)")
    plt.tight_layout()
    plt.show()

# Histogram for population density
def plot_histogram():
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset["density (km²)"], bins=30, kde=True, color="blue", edgecolor="black", alpha=0.7)
    plt.xlabel("Population Density (per km²)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Population Density")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Run the plots
plot_bar_chart()
plot_histogram()

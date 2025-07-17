import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Set the style for seaborn
    sns.set(style="whitegrid")

    # Load a sample dataset
    data = sns.load_dataset("iris")

    # Display the first few rows of the dataset
    print(data.head())

    # Create a pairplot to visualize the relationships in the dataset
    sns.pairplot(data, hue="species")
    
    # Show the plot
    plt.show()
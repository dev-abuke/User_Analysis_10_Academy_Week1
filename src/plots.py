import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys


class Plot:
    def __init__(self) -> None:
        pass

    def plot_pie(self, data, title, label) -> None:
        """Plot pie chart of the data.

        Args:
            data (list): Data to be plotted.
            labels (list): labels of the data.
            colors (list): colors of the data.
        """
        plt.style.context('seaborn-pastel')
        plt.figure(figsize=(8, 8))
        plt.pie(x=data, labels=label, autopct='%1.1f%%', startangle=140)

        plt.title(title)
        plt.show()

    def plot_bar(self, x, y, xlabel,ylabel,title,palette=None) -> None:
        plt.figure(figsize=(12, 6))
        sns.barplot(x=x, y=y, palette="viridis")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)

        plt.show()

    def plot_box(self, df: pd.DataFrame, x_col: str, title: str) -> None:
        """Plot box chart of the column.

        Args:
            df (pd.DataFrame): Dataframe to be plotted.
            x_col (str): column to be plotted.
            title (str): title of chart.
        """
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()
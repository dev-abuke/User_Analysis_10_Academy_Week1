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
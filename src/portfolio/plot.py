import pandas as pd
import matplotlib.pyplot as plt
from src.utils.get_path import get_results_path
from src.portfolio.stats import calc_stats
# %%
RESULTS_PATH = get_results_path()

def plot_distribution(series, title, filename, xlabel = "Returns", ylabel = "Observations"):
    """
    Plot the distribution of a given column in a dataframe.

    Args:
        series (pandas.Series): The series to plot.
        title (str): The title of the plot.
        xlabel (str): The label of the x-axis.
        ylabel (str): The label of the y-axis.
        filename (str): The filename of the plot.
    """

    # Create a figure
    fig, ax = plt.subplots(figsize=(8, 6))
    # Plot the distribution
    series.plot.hist(ax=ax, bins=100, layout="Returns")
    # Set the title and labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


    es, var = calc_stats(series)
    plt.axvline(x=es, color='r', linestyle='--', label='Expected Shortfall')
    plt.axvline(x=var, color='g', linestyle='--', label='Value at Risk')
    plt.legend()

    # Save the figure
    fig.savefig(RESULTS_PATH + "/plots/" + filename)
    # Show the figure
    plt.show()
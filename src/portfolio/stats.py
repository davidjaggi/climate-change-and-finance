import pandas as pd
from src.utils.get_path import get_results_path

RESULTS_PATH = get_results_path()

def calc_stats(returns, filename=None):
    """
    Calculate the statistics for a portfolio.
    """
    # calculate the daily expected shortfall of the portfolio
    quantile = 0.95
    length = len(returns)
    start_obs = round(length * quantile)
    sorted_returns = returns.sort_values(ascending=False)
    tail = sorted_returns.iloc[start_obs:length]
    es = tail.mean()
    var = tail.iloc[0]
    if filename is not None:
        file = open(RESULTS_PATH + "/text/"+ filename + ".txt", 'w')
        print(f"Expected shortfall {es}", file=file)
        print(f"Value at Risk {var}", file=file)
        file.close()
    return es, var




# %%
import pandas as pd
from src.utils.get_path import get_data_path, get_results_path
import matplotlib.pyplot as plt

DATA_PATH = get_data_path()
RESULTS_PATH = get_results_path()
# %%
df = pd.read_csv(DATA_PATH + '/clean/data_elec_returns_clean.csv')
df["Date"] = pd.to_datetime(df["Date"])
df.set_index('Date', inplace=True)
df["returns"] = df.sum(axis=1)
df["cum_returns"] = df["returns"].cumsum()

# %%

plt.plot(df.index, df["cum_returns"])
plt.title("Equally Weighted Portfolio")
plt.xticks(rotation=45)
plt.show()
# %%
plt.savefig(RESULTS_PATH + "/plots/equally_weighted_portfolio.png")
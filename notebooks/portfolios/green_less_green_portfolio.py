# %%
import pandas as pd
from src.utils.get_path import get_data_path, get_results_path
from src.portfolio.stats import calc_stats
from src.portfolio.plot import plot_distribution
import matplotlib.pyplot as plt

DATA_PATH = get_data_path()
RESULTS_PATH = get_results_path()
# %%
df = pd.read_csv(DATA_PATH + '/clean/data_elec_returns_clean.csv')

# filter technology
df_tech = pd.read_csv(DATA_PATH + '/clean/data_tech_clean.csv')
df_tech = df_tech[["isin","exposuretonewenergy"]]

# %%
df["Date"] = pd.to_datetime(df["Date"])
df.set_index('Date', inplace=True)
df["returns"] = df.sum(axis=1)
df["cum_returns"] = df["returns"].cumsum()

# %%
# make barchart of frequency
df_tech["exposuretonewenergy"].value_counts().plot(kind='bar')
plt.title("Exposure to new energy")
plt.xticks(rotation=45)
plt.savefig(RESULTS_PATH + "/plots/exposure_to_new_energy.png")
# %%
isin_a1 = df_tech[df_tech["exposuretonewenergy"] == "A1"]["isin"].to_list()
isin_a2 = df_tech[df_tech["exposuretonewenergy"] == "A2"]["isin"].to_list()
isin_a3 = df_tech[df_tech["exposuretonewenergy"] == "A3"]["isin"].to_list()
isin_a4 = df_tech[df_tech["exposuretonewenergy"] == "A4"]["isin"].to_list()
# %%
df_a1 = df.loc[:, isin_a1].sum(axis=1)
df_a2 = df.loc[:, isin_a2].sum(axis=1)
df_a3 = df.loc[:, isin_a3].sum(axis=1)
df_a4 = df.loc[:, isin_a4].sum(axis=1)
# %%
df_portfolio = pd.concat([df_a1, df_a2, df_a3, df_a4], axis=1)
df_portfolio.columns = ["A1", "A2", "A3", "A4"]
df_portfolio.to_csv(DATA_PATH + "/clean/exposure_rating_portfolio.csv")
# %%
plot_distribution(df_a1, title="A1 Returns", filename="a1_returns")
plot_distribution(df_a2, title="A2 Returns", filename="a2_returns")
plot_distribution(df_a3, title="A3 Returns", filename="a3_returns")
plot_distribution(df_a4, title="A4 Returns", filename="a4_returns")
# %%
calc_stats(df_a1,"a1_returns")
calc_stats(df_a2,"a2_returns")
calc_stats(df_a3,"a3_returns")
calc_stats(df_a4,"a4_returns")

# %%
# calculate cumulative returns
df_a1 = df_a1.cumsum()
df_a2 = df_a2.cumsum()
df_a3 = df_a3.cumsum()
df_a4 = df_a4.cumsum()
# %%
plt.clf()
plt.plot(df.index, df_a1, label="A1")
# plt.plot(df.index, df_a2, label="A2") # no data
plt.plot(df.index, df_a3, label="A3")
plt.plot(df.index, df_a4, label="A4")
plt.legend()
plt.xticks(rotation=45)
plt.title("Cumulative returns of A1, A3 and A4 portfolios")
plt.savefig(RESULTS_PATH + "/plots/exposure_rating_portfolio.png")

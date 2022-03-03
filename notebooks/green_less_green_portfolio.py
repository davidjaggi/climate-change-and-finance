# %%
import pandas as pd
from src.utils.get_path import get_data_path, get_results_path
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
df_a1 = df.loc[:, isin_a1].sum(axis=1).cumsum()
df_a2 = df.loc[:, isin_a2].sum(axis=1).cumsum()
df_a3 = df.loc[:, isin_a3].sum(axis=1).cumsum()
df_a4 = df.loc[:, isin_a4].sum(axis=1).cumsum()
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

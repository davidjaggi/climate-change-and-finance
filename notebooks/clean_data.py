# %%
import pandas as pd
from src.utils.get_path import get_data_path

DATA_PATH = get_data_path()
# %%
# import data
elec = pd.read_csv(DATA_PATH + "/intermediate/data_elec_intermediate.csv")
tech = pd.read_csv(DATA_PATH + "/intermediate/data_tech_intermediate.csv")
index = pd.read_csv(DATA_PATH + "/intermediate/data_index_intermediate.csv")
# %%
# make columnnames lowercase
tech.columns = [x.lower() for x in tech.columns]
# forward fill missing values
elec["Date"] = pd.to_datetime(elec["Date"])
elec.set_index("Date", inplace=True)
elec = elec.sort_index(ascending=True)
# forward fill missing values
elec = elec.fillna(method="ffill", axis=0)
# %%
# exclude if price lower than 1
elec = elec[elec.columns[elec.min() > 1]]
# %%
# clalculate returns
elec_returns = elec.apply(lambda x: x.pct_change(1))
# %%
elec_returns.cumsum().tail(1)
# %%
elec_returns.to_csv(DATA_PATH + "/clean/data_elec_returns_clean.csv")
elec.to_csv(DATA_PATH + "/clean/data_elec_clean.csv")
tech.to_csv(DATA_PATH + "/clean/data_tech_clean.csv")
index.to_csv(DATA_PATH + "/clean/data_index_clean.csv")
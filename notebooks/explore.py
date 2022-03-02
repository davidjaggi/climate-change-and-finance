# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils.get_path import get_data_path, get_results_path
# %%
DATA_PATH = get_data_path()
RESULTS_PATH = get_results_path()

elec = pd.read_csv(DATA_PATH + '/clean/data_elec_returns_clean.csv')
tech = pd.read_csv(DATA_PATH + '/clean/data_tech_clean.csv')
# %%
elec["Date"] = pd.to_datetime(elec["Date"])
elec.set_index("Date", inplace=True)
# %%
elec_describe = elec.describe(include="all")
elec_describe.to_csv(RESULTS_PATH + "/csv/describe_data.csv")
# %%
stock = pd.DataFrame()
stock["ret"] = elec["DE000A1YCMM2"]
stock["cum_ret"] = stock["ret"].cumsum()
plt.plot(stock[["ret","cum_ret"]])
plt.show()



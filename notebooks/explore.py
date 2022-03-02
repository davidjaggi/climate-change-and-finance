# %%
import pandas as pd
import matplotlib.pyplot as plt
from src.utils.get_path import get_data_path
# %%
DATA_PATH = get_data_path()

tech = pd.read_csv(DATA_PATH + '/intermediate/data_tech.csv')
elec = pd.read_csv(DATA_PATH + '/intermediate/data_elec.csv')
# %%
elec.plot()

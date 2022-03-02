# %%
import pandas as pd
from src.utils.get_path import get_data_path
import matplotlib.pyplot as plt

DATA_PATH = get_data_path()
# %%
# import data
elec = pd.read_csv(DATA_PATH + "/intermediate/data_elec_intermediate.csv")
tech = pd.read_csv(DATA_PATH + "/intermediate/data_tech_intermediate.csv")
index = pd.read_csv(DATA_PATH + "/intermediate/data_index_intermediate.csv")
# %%
# make columnnames lowercase
tech.columns = [x.lower() for x in tech.columns]


# %%
elec.to_csv(DATA_PATH + "/clean/data_elec_clean.csv")
tech.to_csv(DATA_PATH + "/clean/data_tech_clean.csv")
index.to_csv(DATA_PATH + "/clean/data_index_clean.csv")
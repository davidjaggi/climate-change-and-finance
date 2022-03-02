# %%
import os
from src.data.extract.load import *
from src.utils.get_path import get_data_path

# %%
df_tech = load_from_excel("data_elec_tech_homework.xlsx")
df_elec = load_from_excel("data_price_elec.xlsx")

# %%
# create lookup table
# we have 56 companies which we have in both datasets
tech_isin = df_tech["ISIN"].to_list()
elec_isin = df_elec.columns.to_list()
# %%
isin_overlap = [x for x in tech_isin if x in elec_isin]

# %%
df_elec = df_elec.loc[:, isin_overlap + ["Date"]]
df_tech = df_tech[df_tech["ISIN"].isin(isin_overlap)]
# %%
df_index = df_tech[["name","ticker","ISIN"]]
df_index.columns = ["name","ticker","isin"]
# %%
# save data to csv
df_elec.to_csv(get_data_path() + "/intermediate/data_elec_intermediate.csv", index=False)
df_tech.to_csv(get_data_path() + "/intermediate/data_tech_intermediate.csv", index=False)
df_index.to_csv(get_data_path() + "/intermediate/data_index_intermediate.csv", index=False)
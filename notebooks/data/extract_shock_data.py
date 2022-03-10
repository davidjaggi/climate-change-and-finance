# %%
import pandas as pd
from src.utils.get_path import get_data_path

DATA_PATH = get_data_path()

# %%
df = pd.read_excel(DATA_PATH + "/raw/exercise_equity_shock.xlsx", sheet_name="NGFS scenarios data")
# remove first column
df = df.iloc[:, 1:]

# %%
df.to_csv(DATA_PATH + "/intermediate/exercise_equity_shock.csv", index=False)
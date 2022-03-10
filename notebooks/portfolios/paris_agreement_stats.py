# %%
import pandas as pd
from src.utils.get_path import get_data_path, get_results_path
import matplotlib.pyplot as plt
from src.portfolio.stats import calc_stats
from src.portfolio.plot import plot_distribution

DATA_PATH = get_data_path()
RESULTS_PATH = get_results_path()
PARIS_AGREEMENT = '2016-04-16' # https://en.wikipedia.org/wiki/Paris_Agreement
df = pd.read_csv(DATA_PATH + '/clean/exposure_rating_portfolio.csv')

# %%
df.head()
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

df_before = df[df.index < PARIS_AGREEMENT]
df_after = df[df.index >= PARIS_AGREEMENT]
# %%
plot_distribution(df_before["A1"], title="A1 Returns before Paris Agreement", filename="a1_returns_before_paris_agreement")
plot_distribution(df_before["A2"], title="A2 Returns before Paris Agreement", filename="a2_returns_before_paris_agreement")
plot_distribution(df_before["A3"], title="A3 Returns before Paris Agreement", filename="a3_returns_before_paris_agreement")
plot_distribution(df_before["A4"], title="A4 Returns before Paris Agreement", filename="a4_returns_before_paris_agreement")
# %%
plot_distribution(df_after["A1"], title="A1 Returns after Paris Agreement", filename="a1_returns_after_paris_agreement")
plot_distribution(df_after["A2"], title="A2 Returns after Paris Agreement", filename="a2_returns_after_paris_agreement")
plot_distribution(df_after["A3"], title="A3 Returns after Paris Agreement", filename="a3_returns_after_paris_agreement")
plot_distribution(df_after["A4"], title="A4 Returns after Paris Agreement", filename="a4_returns_after_paris_agreement")
# %%
calc_stats(df_before["A1"],"a1_returns_before_paris_agreement")
calc_stats(df_before["A2"],"a2_returns_before_paris_agreement")
calc_stats(df_before["A3"],"a3_returns_before_paris_agreement")
calc_stats(df_before["A4"],"a4_returns_before_paris_agreement")
# %%
calc_stats(df_after["A1"],"a1_returns_after_paris_agreement")
calc_stats(df_after["A2"],"a2_returns_after_paris_agreement")
calc_stats(df_after["A3"],"a3_returns_after_paris_agreement")
calc_stats(df_after["A4"],"a4_returns_after_paris_agreement")
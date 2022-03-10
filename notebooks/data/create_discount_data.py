# %%
from src.utils.get_path import get_data_path
import pandas as pd

# %%
DATA_PATH = get_data_path()
DISCOUNT_RATE = 0.01
VALUTAION_DATE = '2020-01-01'


df = pd.read_csv(DATA_PATH + '/intermediate/exercise_equity_shock.csv')
# delete unit and region
df = df.drop(columns=['Unit', 'Region'])
df_zero = df[df['Scenario'] == "Net Zero 2050"]
df_current = df[df['Scenario'] == "Current Policies"]
df_delayed = df[df['Scenario'] == "Delayed transition"]

# %%
def discount_series(series, discount_rate, valuation_date):
    # iterate over series
    disc_series = []
    # take year from valuation date as integer
    valuation_year = int(pd.to_datetime(valuation_date).year)
    print(f"Valuation year: {valuation_year}")

    for i in range(len(series)):
        # get current value
        value = series.iloc[i]
        # get year
        # take year from index as integer
        year = int(series.index[i].year)
        # get discount factor
        discount_factor = (1 + discount_rate) ** (year - valuation_year)
        # set new value
        disc_series.append(value / discount_factor)
    return disc_series

# %%
# drop Scenatio column
df_zero = df_zero.drop(columns=['Scenario'])
df_zero = df_zero.melt(id_vars=['Variable'], var_name='Year', value_name='Value')
df_zero['year'] = pd.to_datetime(df_zero['Year'], format='%Y')
df_zero.set_index('year', inplace=True)
df_zero["Discount"] = discount_series(df_zero['Value'], DISCOUNT_RATE, VALUTAION_DATE)
# %%
# drop Scenatio column
df_current = df_current.drop(columns=['Scenario'])
df_current = df_current.melt(id_vars=['Variable'], var_name='Year', value_name='Value')
df_current['year'] = pd.to_datetime(df_current['Year'], format='%Y')
df_current.set_index('year', inplace=True)
df_current["Discount"] = discount_series(df_current['Value'], DISCOUNT_RATE, VALUTAION_DATE)
# %%
# drop Scenatio column
df_delayed = df_delayed.drop(columns=['Scenario'])
df_delayed = df_delayed.melt(id_vars=['Variable'], var_name='Year', value_name='Value')
df_delayed['year'] = pd.to_datetime(df_delayed['Year'], format='%Y')
df_delayed.set_index('year', inplace=True)
df_delayed["Discount"] = discount_series(df_delayed['Value'], DISCOUNT_RATE, VALUTAION_DATE)

# %%
df_zero.to_csv(DATA_PATH + '/clean/discount_zero.csv')
df_current.to_csv(DATA_PATH + '/clean/discount_current.csv')
df_delayed.to_csv(DATA_PATH + '/clean/discount_delayed.csv')

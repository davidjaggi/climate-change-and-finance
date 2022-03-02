import pandas
from src.utils.get_path import *

def load_from_excel(file_name):
    """
    Loads data from an excel file.
    """
    path = get_data_path()
    df = pandas.read_excel(path +"/raw/" + file_name, "Sheet1")
    return df

if __name__ == "__main__":
    df = load_from_excel("data_price_elec.xlsx")
    print(df)

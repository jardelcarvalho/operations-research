import pandas as pd

def load_data(path, sep=','):
    return pd.read_csv(path, sep=sep)

def write_data():
    pass
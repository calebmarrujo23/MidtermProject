import pandas as pd

class PlayerNotFoundError(Exception):
    """If a player cant be found it will give an error"""
    pass

def load_baseball_data(file_path):
    """
    Gives us mlb players from csv data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e

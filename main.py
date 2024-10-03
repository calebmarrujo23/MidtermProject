#https://baseballsavant.mlb.com/csv-docs
#link above is the data set I used for hitting and pitching
#

from player_stats import load_baseball_data
from sorting import (
    sort_by_strikeouts_pitchers,
    sort_by_walks_pitchers,
    sort_by_strikeouts_hitters,
    sort_by_walks_hitters,
    sort_by_woba,
)
from user import get_user_input
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

HITTING_DATA_PATH = './data/hitting.csv'
PITCHING_DATA_PATH = './data/pitching.csv'


def main():
    print("\nWelcome to the MLB Stats Program!")
    print("1. Analyze hitting statistics")
    print("2. Analyze pitching statistics")
    print("3. Search for a player's stats")

    choice = input("\nPlease enter your choice (1-3): ")

    if choice == '1':
        data = load_baseball_data(HITTING_DATA_PATH)
        print("\n1. Show top hitters by strikeout percentage")
        print("2. Show top hitters by walk percentage")
        print("3. Show top hitters by wOBA")

        sub_choice = input("\nPlease enter your choice (1-3): ")
        if sub_choice == '1':
            sorted_data = sort_by_strikeouts_hitters(data)
            print(sorted_data.head(10))
        elif sub_choice == '2':
            sorted_data = sort_by_walks_hitters(data)
            print(sorted_data.head(10))
        elif sub_choice == '3':
            sorted_data = sort_by_woba(data)
            print(sorted_data.head(10))

    elif choice == '2':
        data = load_baseball_data(PITCHING_DATA_PATH)
        print("\n1. Show top pitchers by strikeout percentage")
        print("2. Show top pitchers by walk percentage")

        sub_choice = input("\nPlease enter your choice (1-2): ")
        if sub_choice == '1':
            sorted_data = sort_by_strikeouts_pitchers(data)
            print(sorted_data.head(10))
        elif sub_choice == '2':
            sorted_data = sort_by_walks_pitchers(data)
            print(sorted_data.head(10))

    elif choice == '3':
        dataset_type = input("Which dataset do you want to search (hitting/pitching)? ").strip().lower()
        if dataset_type == 'hitting':
            data = load_baseball_data(HITTING_DATA_PATH)
        elif dataset_type == 'pitching':
            data = load_baseball_data(PITCHING_DATA_PATH)
        else:
            print("Invalid dataset type.")
            return

        print("Column names in the dataset:", data.columns)

        if 'last_name, first_name' in data.columns:
            data[['last_name', 'first_name']] = data['last_name, first_name'].str.split(', ', expand=True)

        player_name = get_user_input()
        if 'last_name' in data.columns:
            player_stats = data[data['last_name'].str.contains(player_name, case=False, na=False)]

            if player_stats.empty:
                print(f"No player found with the name '{player_name}'.")
            else:
                print(player_stats)
        else:
            print("Error: 'last_name' column not found in the dataset.")


if __name__ == "__main__":
    main()

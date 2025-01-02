import pandas as pd
import json
import mysql.connector 
from pymongo import MongoClient

"""
    This script was created specifically for setting up the PokeMart database. 
    NOTE: Run this script AFTER the pokeapi database retrieval script.
"""

INPUT_FILENAME = "data/initial_inventory.json"
EXCLUDED_CATEGORIES = ['Flutes', 'Collectibles', 'Loot', 'Mulch', 
                       'All Mail', 'Baking Only', 'Effort Drop', 
                       'Type Protection', 'In A Pinch', 'Other', 
                       'Plates', 'Apricorn Box', 'Gameplay', 'Jewels', 
                       'Memories', 'Catching Bonus', 'Species Candies', 
                       'Curry Ingredients', 'Nature Mints', 'Dynamax Crystals',
                       'Tera Shard', 'Sandwich Ingredients', 'Tm Materials',
                       'Picnic', 'Plot Advancement']

def load_data():
    data = pd.read_json(INPUT_FILENAME)
    return data

def exclude_categories(data: pd.DataFrame) -> any:
    # included_categories = [category for category in data['category'].unique() if category not in EXCLUDED_CATEGORIES]
    cleaned_data = data[~data['category'].isin(EXCLUDED_CATEGORIES)].dropna()
    # print(included_categories)
    return cleaned_data

def main():
    data = exclude_categories(load_data())
    print(data)

if __name__ == "__main__":
    main()
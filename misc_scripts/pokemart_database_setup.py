import os
import mysql.connector.cursor
import pandas as pd
import json
import mysql.connector 
from pymongo import MongoClient
from config import *
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

# MYSQL_USER = os.getenv('MYSQL_USER')
# MYSQL_PASS = os.getenv('MYSQL_PASS')
# MONGODB_CLIENT = os.getenv('MONGODB_CLIENT')

def load_data():
    data = pd.read_json(INPUT_FILENAME)
    return data

def clean_data(data: pd.DataFrame) -> any:
    data_without_excluded_categories = data[~data['category'].isin(EXCLUDED_CATEGORIES)]
    data_without_empty_columns = data_without_excluded_categories.dropna()
    return data_without_empty_columns

def generate_statement_for_categories(data: pd.DataFrame) -> str:
    query = "INSERT INTO Item_Categories (cat_name) VALUES "
    columns = data['category'].unique().tolist()
    length = len(columns)
    for index, column in enumerate(columns):
        query = query + f"(\'{column}\')"
        if index == length - 1:
            query += ';'
        else:
            query += ','

    return query

def initialize_database(data: pd.DataFrame) -> None:
    msql_connection = mysql.connector.connect(host='localhost', user=MYSQL_USER, password=MYSQL_PASS, database='pokemart')
    msql_cursor = msql_connection.cursor()

    queries = []
    queries.append(generate_statement_for_categories(data))

    for query in queries:
        msql_cursor.execute(query)
        msql_connection.commit()

    
    
    msql_cursor.close()
    msql_connection.close()

def main():
    raw_data = load_data()
    cleaned_data: pd.DataFrame = clean_data(raw_data)
    initialize_database(cleaned_data)



if __name__ == "__main__":
    main()
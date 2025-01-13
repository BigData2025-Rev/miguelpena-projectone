import os
import pandas as pd
import json
# from config import *
"""
    This script was created specifically for generating the seed.sql file that 
    will be used in the seed.py file for seeding the database with PokeApi data. 
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
    query = "INSERT INTO Item_Categories (name, slug) VALUES "
    columns = data['category'].unique().tolist()
    length = len(columns)
    for index, column in enumerate(columns):
        query = query + f"(\'{column}\', \'{column.replace(' ', '-').lower()}\')"
        if index == length - 1:
            query += ';\n'
        else:
            query += ',\n\t'

    return query

def generate_statement_for_items(data: pd.DataFrame) -> str:
    updated_data = data.drop(columns=['sprite', 'effect', 'category'])
    query = "INSERT INTO Items (name, cost) VALUES "
    length = updated_data.shape[0]
    for index, row in updated_data.iterrows():
        query = query + f"(\'{row['name']}\', {row['cost']})"
        if index == length - 1:
            query += ';\n'
        else:
            query += ',\n\t'

    return query
    # data.drop('category')

def generate_statement_for_item_category_relational(data: pd.DataFrame) -> str:
    category_ids = {value:index+1 for index, value in enumerate(data['category'].unique().tolist())}
    item_ids = {value:index+1 for index, value in enumerate(data['name'].tolist())}
    updated_data = data.replace(category_ids).replace(item_ids).drop(columns=['cost', 'sprite', 'effect'])
    query = "INSERT INTO Items_Category_Relational (item_id, item_category_id) VALUES "
    length = updated_data.shape[0]
    for index, row in updated_data.iterrows():
        query = query + f"({row['name']}, {row['category']})"
        if index == length - 1:
            query += ';\n'
        else:
            query += ',\n\t'

    return query

def create_seed_file(data: pd.DataFrame) -> None:
    queries = []
    queries.append(generate_statement_for_categories(data))
    queries.append(generate_statement_for_items(data))
    queries.append(generate_statement_for_item_category_relational(data))

    with open('backend/seed.sql', 'w') as file:
        file.writelines(queries)


def main():
    raw_data = load_data()
    cleaned_data: pd.DataFrame = clean_data(raw_data)
    create_seed_file(cleaned_data)



if __name__ == "__main__":
    main()
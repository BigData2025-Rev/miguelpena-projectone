import pandas as pd
from tqdm import tqdm 
import requests
import json

#dependencies:
#pip install tqdm
#pip install pandas


ITEM_LIMIT = 2229

def retrieve_item_details(item_id: int) -> any:
    api_url = "https://pokeapi.co/api/v2/item/"
    result = api_url + str(item_id)
    response_api = requests.get(result)
    if response_api.status_code != 200:
        return None
    # print(response_api.status_code)
    data = response_api.text
    parsed_data = json.loads(data)
    return parsed_data

def get_item_name(parsed_data: any) -> str:
    names_list = parsed_data['names']
    for name in names_list:
        if name['language']['name'] != 'en':
            continue
        return name['name']
    
def get_item_cost(parsed_data: any) -> int:
    return parsed_data['cost']    

def get_item_category(parsed_data: any) -> str:
    raw_string = str(parsed_data['category']['name'])
    return raw_string.replace('-', ' ').title()

def get_item_sprite(parsed_data: any) -> str:
    return parsed_data['sprites']['default']

def get_item_effect(parsed_data: any) -> str:
    effect_entries = parsed_data['effect_entries']
    for entry in effect_entries:
        if entry['language']['name'] != 'en':
            continue
        return entry['effect']

def clean_item_details(parsed_data: any) -> any:
    item_name = get_item_name(parsed_data)
    item_cost = get_item_cost(parsed_data)
    item_sprite = get_item_sprite(parsed_data)
    item_effect = get_item_effect(parsed_data)
    item_category = get_item_category(parsed_data)
    cleaned_item = {'name':[item_name],
                    'cost':[item_cost],
                    'sprite':[item_sprite],
                    'effect':[item_effect],
                    'category':[item_category]}
    return cleaned_item

def save_inventory(inventory: any) -> None:
    filename = 'initial_inventory.json'
    inventory.to_json(filename, orient='records', indent=4)

def main():
    inventory_set = False
    inventory: pd.DataFrame | None = None
    for index in tqdm(range(1,ITEM_LIMIT)):
        raw_data = retrieve_item_details(index)
        if raw_data == None:
            continue
        if raw_data['cost'] == 0:
            continue
        clean_data = clean_item_details(raw_data)
        item_df = pd.DataFrame(clean_data)
        if not inventory_set:
            inventory = item_df
            inventory_set = True
        else:
            inventory = pd.concat([inventory, item_df], ignore_index=True)
    
    save_inventory(inventory)
    print(inventory)

if __name__ == '__main__':
    main()



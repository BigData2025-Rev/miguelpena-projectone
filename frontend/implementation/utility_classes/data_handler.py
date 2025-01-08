import os
import pandas as pd
from interface.dataaccess_interfaces.data_interface import IData

class DataHandler(IData):
    def __init__(self, filename):
        self.data = None
        self.filename = f'data/{filename}'

    def update_data(self, data: pd.DataFrame) -> pd.DataFrame:
        self.data = data
        return data
    
    def save(self):
        if self.data == None: 
            return 
        self.data.to_json(self.filename, orient='split', compression='infer')
    
    def load(self) -> pd.DataFrame:
        self.data = pd.read_json(self.filename, orient='split', compression='infer')
        return self.data
    
    # def set_filename(self, filename: str):
    #     self.filename = f'data/{filename}'
    
    # def get_data(self) -> pd.DataFrame:
    #     return self.data
import os
import pandas as pd
import requests
import logging
from requests import Response
from interface.dataaccess_interfaces.data_interface import IData
from config import FLASK_RUN_PORT
logger = logging.getLogger(__name__)

class DataHandler(IData):

    def update_data(self, data: dict) -> dict:
        """
            Expects the data to be in the correct schema, errors otherwise and handled appropriately.
        """
        self.data = data
        return data
    
    def get(self):
        if self.data == None: 
            return 
        
        self.data.to_json(self.filename, orient='split', compression='infer')
        self.data.
    
    def post(self):
        headers = {'Authorization': self.access_token}
        response: Response = requests.post(f"https://localhost:{FLASK_RUN_PORT}{self.endpoint}", headers=headers, json=self.data)
        self.handle_errors(response)
        self.handle_response(response)

    def load(self) -> pd.DataFrame:
        self.data = pd.read_json(self.filename, orient='split', compression='infer')
        return self.data
    
    
        

        
        # try:
        #     response.raise_for_status()
        # except requests.exceptions.HTTPError as e:
        #     logger.warning(e.)
    
    # def set_filename(self, filename: str):
    #     self.filename = f'data/{filename}'
    
    # def get_data(self) -> pd.DataFrame:
    #     return self.data
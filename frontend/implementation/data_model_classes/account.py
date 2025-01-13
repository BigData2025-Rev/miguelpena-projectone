import logging
import pandas as pd
import requests
from requests import Response, HTTPError
from dataclasses import dataclass
from implementation.utility_classes import DataHandler
from config import FLASK_RUN_PORT

logger = logging.getLogger(__name__)

@dataclass(init=False)
class Account():

    def to_dataframe(self) -> pd.DataFrame:
        df_precursor = {'username':[self.data.get('username')],
                        'password':[self.data.get('password')],
                        }
                        
        df: pd.DataFrame = pd.DataFrame(df_precursor)
        return df

class CreateAccount(DataHandler):
    
    def __init__(self, username, password):
        self.data = {'username': username, 'password': password}
        self.endpoint = '/auth/register'
        self.success = False
        logger.info('Sending request to create account...')
        self.post()

    def post(self):
        response: Response = requests.post(f"https://localhost:{FLASK_RUN_PORT}{self.endpoint}", json=self.data)
        self.handle_errors(response)
        if not self.success:
            return
        self.handle_response(response)


    def handle_errors(self, response: Response):
        if response.status_code == 200:
            self.success = True
            return
        
        if response.status_code != 400:
            logger.warning('Attempt to create account failed.')
            return
        
        logger.info('Failed to create account.')
        print('Please fix the following:')
        for key in self.data.keys():
            print(f'{key.capitalize()}: {response.json().get(key)}')

    def handle_response(self, response: Response):
        data = response.json()
        print(data.get('msg'))
        logger.info(data.get('msg'))

class LoginAccount(DataHandler):
    
    def __init__(self, username, password):
        self.data = {'username':username, 'password': password}
        self.endpoint = '/auth/login'
        self.access_token = ""
        self.refresh_token = ""
        self.post()

    def post(self):
        response: Response = requests.post(f"https://localhost:{FLASK_RUN_PORT}{self.endpoint}", json=self.data)
        self.handle_errors(response)
        self.handle_response(response)
    
    def handle_errors(self, response: Response):
        if response.status_code == 200:
            self.success = True
            return
        
        if response.status_code != 400:
            logger.warning('Attempt to login failed, due to internal error.')
            return
        
        logger.info('Login failed.')
        print(response.json().get('msg'))

    def handle_response(self, response: Response):
        tokens = response.json()
        self.access_token = tokens.get('access_token')
        self.refresh_token = tokens.get('refresh_token')
        


    

    
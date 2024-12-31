import pandas as pd
from abc import ABC, abstractmethod
from implementation.data_model_classes.account import Account

class IAccountDataAccess(ABC):
    
    @abstractmethod
    def get_account_by_username(self, username: str) -> Account:
        pass
    
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass
    
    @abstractmethod
    def update_account(self, account: Account) -> bool:
        pass

    @abstractmethod
    def delete_account_by_username(self, username: str) -> bool:
        pass
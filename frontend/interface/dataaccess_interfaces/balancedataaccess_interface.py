import pandas as pd
from abc import ABC, abstractmethod
from implementation.data_model_classes.balance import Balance

class IBalanceDataAccess(ABC):
    
    @abstractmethod
    def get_balance_by_username(self, username: str) -> Balance:
        pass
    
    @abstractmethod
    def create_balance(self, balance: Balance) -> Balance:
        pass
    
    @abstractmethod
    def update_balance(self, balance: Balance) -> bool:
        pass

    @abstractmethod
    def delete_balance_by_username(self, username: str) -> bool:
        pass
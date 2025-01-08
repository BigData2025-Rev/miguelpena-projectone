import pandas as pd
from abc import ABC, abstractmethod
from implementation.data_model_classes.expense import Expense

class IExpenseDataAccess(ABC):
    
    @abstractmethod
    def get_expense_by_username(self, username: str) -> Expense:
        pass
    
    @abstractmethod
    def create_expense(self, expense: Expense) -> Expense:
        pass
    
    @abstractmethod
    def update_expense(self, expense: Expense) -> bool:
        pass

    @abstractmethod
    def delete_expense_by_username(self, username: str) -> bool:
        pass
import pandas as pd
from implementation.data_model_classes.expense import Expense
from interface.dataaccess_interfaces.expensedataaccess_interface import IExpenseDataAccess
from implementation.utility_classes.data_handler import DataHandler

class ExpenseDAO(IExpenseDataAccess):
    def __init__(self):
        filename = 'expenses.json'
        self.data_handler = DataHandler(filename)

    def get_expense_by_username(self, username: str) -> Expense:
        pass
        #df: pd.DataFrame = self.data_handler.load()
        # entry = df.loc[df['account_username']==username]
        # return Account(entry['account_id'][0], entry['account_username'][0], 
        #                entry['account_password'][0], entry['first_name'][0],
        #                entry['last_name'][0], entry['monthly_income'][0])
    
    def create_account(self, account: Expense) -> Expense:
        pass
        # df: pd.DataFrame = account.to_dataframe()
        # if self.data_handler.update_data(df):
        #     self.data_handler.save()
        #     return account
        # else:
        #     return None
        

    # def update_account(self, account: Account) -> bool:
    #     pass

    # def delete_account_by_username(self, username: str) -> bool:
    #     pass



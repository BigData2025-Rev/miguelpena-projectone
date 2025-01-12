import pandas as pd
import requests
from dataclasses import dataclass
# from implementation.utility_classes.hashing import Hashing

@dataclass(init=False)
class Account():
    """
        This data class will be used to model accounts.
    """

    # id: int
    username: str
    password: str
    # first_name: str
    # last_name: str
    # monthly_income: float

    # def check_matching_password(self, entered_password) -> bool:
    #     hashed_object = Hashing()
    #     hashed_object.set_hashed_string(self.account_password)
    #     return hashed_object.is_a_match(entered_password)
    
    # def hash_password(self, new_password: str):
    #     hashed_object = Hashing(new_password)
    #     self.account_password = hashed_object.get_hashed_string()
    def __init__(self, username, password):
        response = requests.get()

    def to_dataframe(self) -> pd.DataFrame:
        df_precursor = {'username':[self.account_username], #'account_id':[self.account_id],
                        'password':[self.account_password]
                       }
                        # 'first_name':[self.first_name], 
                        # 'last_name':[self.last_name], 
                        # 'monthly_income':[self.monthly_income]}
        df: pd.DataFrame = pd.DataFrame(df_precursor)
        return df

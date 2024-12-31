import pandas as pd
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Expense():
    """
        This data class will be used to model expenses. 
    """
    account_username: str
    amount: float
    timestamp: datetime
    category: int

    def to_dataframe(self) -> pd.DataFrame:
        df_precursor = {'account_username':[self.account_username],
                        'amount':[self.amount], 
                        'timestamp':[self.timestamp],
                        'category':[self.category]}
        df: pd.DataFrame = pd.DataFrame(df_precursor)
        return df
import pandas as pd
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Balance():
    """
        This data class will be used to model balance for keeping track of the current monthly income minus expenses. 
    """
    account_username: str
    amount: float
    timestamp: datetime

    def to_dataframe(self) -> pd.DataFrame:
        df_precursor = {'account_username':[self.account_username],
                        'amount':[self.amount], 
                        'timestamp':[self.timestamp]}
        df: pd.DataFrame = pd.DataFrame(df_precursor)
        return df
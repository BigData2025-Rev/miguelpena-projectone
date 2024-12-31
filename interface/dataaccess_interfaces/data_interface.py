import pandas as pd
from abc import ABC, abstractmethod

class IData(ABC):
    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def load(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def update_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass
    # @abstractmethod
    # def set_filename(self, filename: str) -> None:
    #     pass
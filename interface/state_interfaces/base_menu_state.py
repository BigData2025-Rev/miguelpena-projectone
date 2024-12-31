from abc import ABC, abstractmethod

class BaseMenuState(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass
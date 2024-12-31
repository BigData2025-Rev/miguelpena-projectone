from abc import ABC, abstractmethod

class IHash(ABC):
    @abstractmethod
    def set_hashed_string(self, hashed_input: str) -> str:
        pass
    
    @abstractmethod
    def get_hashed_string(self) -> str:
        pass
    
    @abstractmethod
    def is_a_match(self, input_string) -> bool:
        pass
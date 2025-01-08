import bcrypt
#pip install bcrypt
from interface.utility_interfaces.hashing_interface import IHash

class Hashing(IHash):
    def __init__(self, input_string: str | None):
        """
            When creating an object of this class, provide the string that will be hashed.
        """
        if input_string != None:
            hashed_value: bytes = bcrypt.hashpw(input_string.encode(), bcrypt.gensalt())
        
        self.hashed_value = hashed_value.decode()
    
    def set_hashed_string(self, hashed_input: str) -> str:
        self.hashed_value = hashed_input

    def get_hashed_string(self) -> str:
        return self.hashed_value
    
    def is_a_match(self, input_string) -> bool:
        return self.check_match(input_string, self.hashed_value)
    
    @staticmethod
    def check_match(input_string: str, hashed_string: str) -> bool:
        return bcrypt.checkpw(input_string.encode(), hashed_string.encode())
import re
from interface.utility_interfaces.input_validation_interface import IInputValidation
from implementation.enum_classes.validation_type import ValidationType

from custom_exceptions.invalid_number_input import InvalidNumberInput
from custom_exceptions.invalid_menu_selection import InvalidMenuSelection
from custom_exceptions.invalid_string_input import InvalidStringInput

class InputValidation(IInputValidation):
    def __init__(self, input: str, validation_type: int, **kwargs: any):
        """
            When creating instance of this class, include the input and validation type enum class.
            :params: input -> string, validation_type -> enum of validation, eg. 1 -> IsANumber, 2 -> IsAMenuItem
        """
        self.input = input
        self.validation_type = validation_type
        self.validation_criteria = dict(kwargs)
    
    def check_if_float(self) -> bool:
        try: 
            if float(self.input) < 0:
                raise InvalidNumberInput("Please enter a positive number.")
            return True
        except ValueError as ve:
            raise InvalidNumberInput("Please enter a number.")

    def check_if_integer(self) -> bool:
        try:
            if int(self.input) < 0:
                raise InvalidNumberInput("Please enter a positive number.")
            return True
        except ValueError as e:
            return self.check_if_float()

    def check_if_number(self) -> bool:
        # """
        #     This method uses regular expression to ensure that user input is a number.
        #     As a refresher here are a few rules: 
        #     \d -> matches 0-9 
        #     + -> one or more 
        #     ? -> zero or one
        #     ^ -> starts with following re expression
        #     $ -> ends with prior re expression
        #     \ -> followed by a character indicates a specific character, 
        #     for example \- specifies that I'm looking for the negative sign, or \. indicates 
        #     a period and not the re symbol for matching any character.
        # """
        numeric_format = re.compile(r'^\-?\d+\.?\d+$')
        match_obj = re.search(numeric_format, self.input)
        if match_obj == None:
            raise InvalidNumberInput("Please enter a number.")
        self.input = match_obj.group()
        
        return self.check_if_integer()

    def check_if_menu_option(self) -> bool:
        valid_chars = self.validation_criteria.get('valid_options')
        if valid_chars == None:
            raise InvalidMenuSelection("Please provide a valid string of characters.")
        
        if len(self.input) > 1 or self.input.lower() not in valid_chars.lower():
            raise InvalidMenuSelection("Please enter a corresponding character.")
        
        return True

    def check_if_valid_string(self) -> bool:
        reject_short = self.validation_criteria.get('reject_short')
        can_contain_numbers = self.validation_criteria.get('can_contain_numbers')
        if reject_short == None or can_contain_numbers == None:
            raise InvalidStringInput("Please include the appropriate boolean values.")
        
        if reject_short and len(self.input) <= 2:
            raise InvalidStringInput("The string you entered was too short.")

        if not can_contain_numbers and not self.input.isalpha():
            raise InvalidStringInput("Your entered text cannot contain numbers or symbols.")

        return True

    def is_valid(self) -> bool:
        match(self.validation_type):
            case ValidationType.IsANumber:
                return self.check_if_number()
            case ValidationType.IsAMenuOption:
                return self.check_if_menu_option()
            case ValidationType.IsValidString:
                return self.check_if_valid_string()
            case _:
                return False

    def get_value(self) -> str:
        return self.input
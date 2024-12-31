from abc import abstractmethod
from custom_exceptions.invalid_string_input import InvalidStringInput
from custom_exceptions.invalid_number_input import InvalidNumberInput
from interface.menu_interfaces.submenu_interface import ISubMenu
from implementation.utility_classes.input_validation import InputValidation
from implementation.enum_classes.validation_type import ValidationType
from implementation.enum_classes.submenu_state import SubMenuState

class BaseInputSubmenu(ISubMenu):

    def display(self):
        # user_input = dict()
        input_valid = False
        validation: InputValidation | None = None
        for current in self.display_submenu():
            self.current_validation = self.submenu_options[current][1]
            while not input_valid:
                input_valid, validation = self.handle_input()
        
        print('Valid Input')
        
    def handle_input(self) -> tuple[bool,InputValidation]:
        input_valid = False
        user_input = input('')
        validation: InputValidation | None = None
        # valid_options = self.get_valid()
        try: 
            match(self.current_validation):
                case ValidationType.IsValidString:
                    input_valid, validation = BaseInputSubmenu.handle_string(user_input)
                case ValidationType.IsANumber:
                    input_valid, validation = BaseInputSubmenu.handle_number(user_input)
        except (InvalidStringInput, InvalidNumberInput) as e:
            print(e.message)
        finally: 
            return input_valid, validation
        
   

    def get_state(self) -> int:
        return self.current_state
    
    @staticmethod
    def handle_string(string_input: str) -> bool:
        validation = InputValidation(string_input, ValidationType.IsValidString, reject_short=True, can_contain_numbers=True)
        return validation.is_valid(), validation

    @staticmethod
    def handle_number(number_input: str) -> bool:
        validation = InputValidation(number_input, ValidationType.IsANumber)
        return validation.is_valid(), validation
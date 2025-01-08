import string
from implementation.utility_classes.input_validation import InputValidation
from implementation.enum_classes.validation_type import ValidationType
from custom_exceptions.invalid_menu_selection import InvalidMenuSelection

from interface.menu_interfaces.base_submenu import BaseSubmenu

class LoggedInService(BaseSubmenu):
    
    def __init__(self, name: str):
        # self.current_state = SubMenuState.INITIAL
        self.submenu_options = ['Report Expense', 'Show History and Stats', 'Update Monthly Income', 'Close Application']
        self.selected_option = None
        self.name = name
    
    def display_submenu(self):
        
        print(f"\n\tWelcome to {self.name}!\n\tWhat would you lke to do?\n")
        
        for index, option in enumerate(self.submenu_options):
            print(f'\t{string.ascii_uppercase[index]}. {option}')

    def get_valid(self) -> str:
        return string.ascii_uppercase[:len(self.submenu_options)]
    
    # def perform_selected_option(self):
    #     selected_index = string.ascii_lowercase.find(self.selected_option)
    #     listed_actions = [
    #         lambda _: self.create_account(),
    #         lambda _: self.login(),
    #         lambda _: self.close()
    #     ]
    #     listed_actions[selected_index]()

    # def create_account(self):
    #     pass

    # def login(self):
    #     pass

    def close(self):
        pass

    


    


        

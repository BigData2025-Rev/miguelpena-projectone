from abc import abstractmethod
from custom_exceptions.invalid_menu_selection import InvalidMenuSelection
from interface.menu_interfaces.submenu_interface import ISubMenu
from implementation.utility_classes.input_validation import InputValidation
from implementation.enum_classes.validation_type import ValidationType
from implementation.enum_classes.submenu_state import SubMenuState

class BaseSubmenu(ISubMenu):

    def display(self):
        
        input_valid = False
        validation: InputValidation | None = None

        while not input_valid:
            self.display_submenu()
            input_valid, validation = self.handle_input()

        self.selected_option = validation.get_value()
        self.perform_selected_option()

    def handle_input(self) -> tuple[bool, InputValidation | None]:
        input_valid = False
        user_input = input('\n>>>')
        valid_options = self.get_valid()
        validation = InputValidation(user_input, ValidationType.IsAMenuOption, valid_options=valid_options)
        try:
            if validation.is_valid():
                input_valid = True
        except InvalidMenuSelection as e:
            print(e.message)
        finally: 
            return input_valid, validation

    # def get_state(self) -> int:
    #     return self.current_state
    
    @abstractmethod
    def perform_selected_option(self) -> None:
        pass

    @abstractmethod
    def get_valid(self) -> str:
        pass
    
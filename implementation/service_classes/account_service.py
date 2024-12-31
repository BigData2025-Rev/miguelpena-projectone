import string
from implementation.enum_classes.validation_type import ValidationType
from implementation.data_access_classes.account_dao import AccountDAO

from interface.menu_interfaces.base_submenu import BaseSubmenu
# from implementation.enum_classes.submenu_state import SubMenuState

class AccountService(BaseSubmenu):
    def __init__(self):
        self.account_dao = AccountDAO()
        # self.current_state = SubMenuState.INITIAL
        self.submenu_options = [('Username: ', ValidationType.IsValidString),
                                ('Password: ', ValidationType.IsValidString), 
                                ('Renter Password: ', ValidationType.IsValidString), 
                                ('Monthly Income: ', ValidationType.IsANumber)]

    def display_submenu(self):
        
        print(f"\n\tCreating Account\n\tPlease enter the following:\n")
        
        for current, option in enumerate(self.submenu_options):
            print(f'\t{option[0]}', end='')
            yield current

    def get_valid(self) -> str:
        return string.ascii_uppercase[:len(self.submenu_options)]

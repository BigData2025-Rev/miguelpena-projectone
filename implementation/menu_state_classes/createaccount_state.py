from interface.state_interfaces.base_menu_state import BaseMenuState
from implementation.service_classes.account_service import AccountService
from implementation.main_menu import MainMenu

class CreateAccountState(BaseMenuState):
    def __init__(self, menu: MainMenu):
        self.menu = menu
        self.submenu = AccountService()

    def execute(self):
        self.submenu.display()
    
    def close(self):
        self.menu.current_state = self.menu.initial_state
from interface.state_interfaces.base_menu_state import BaseMenuState
from implementation.service_classes.initial_service import InitialService
# from implementation.main_menu import MainMenu

class InitialState(BaseMenuState):
    def __init__(self, menu):
        self.menu = menu
        self.submenu = InitialService(menu.get_name())

    def execute(self):
        self.submenu.display()
    
    def close(self):
        self.menu.current_state = self.menu.initial_state
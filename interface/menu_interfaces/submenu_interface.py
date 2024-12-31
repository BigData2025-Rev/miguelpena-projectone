from abc import ABC, abstractmethod
# from implementation.enum_classes.submenu_state import SubMenuState

class ISubMenu(ABC):
    # def run(self) -> None:
    #     match(self.current_state):
    #         case SubMenuState.INITIAL:
    #             self.display()
    #         case _:
    #             print('Closing...')
    
    @abstractmethod
    def display(self) -> None:
        pass

    # @abstractmethod
    # def get_state(self) -> int:
    #     pass
    
    @abstractmethod
    def display_submenu(self) -> None:
        pass
    
   
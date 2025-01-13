import logging
from implementation.main_menu import MainMenu
from implementation.enum_classes.mainmenu_state import MainMenuState
from custom_exceptions import *
logger = logging.getLogger(__name__)

def main() -> None:
    """
        Program entry point, should handle exceptions at the highest level,
        and run the menu logic as needed.  
    """
    logging.basicConfig(filename='pokemart.log', level=logging.INFO, format='%(asctime)s :: %(message)s')
    logger.info('Pok\xE9Mart CLI App Started')
    
    menu: MainMenu = MainMenu("Pok\xE9Mart")
    while (menu.get_state() != MainMenuState.CLOSING):
        try:
            menu.run()
        except (InvalidLoginCredentials, InvalidMenuSelection, InvalidNumberInput, InvalidStringInput) as e:
            print(e.message)

    logger.info('Pok\xE9Mart CLI App Closed')
if __name__ == "__main__":
    main()
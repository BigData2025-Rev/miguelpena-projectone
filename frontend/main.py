from implementation.main_menu import MainMenu
from implementation.enum_classes.mainmenu_state import MainMenuState
from custom_exceptions.invalid_login_credentials import InvalidLoginCredentials

def main() -> None:
    """
        Program entry point, should handle exceptions at the highest level,
        and run the menu logic as needed.  
    """
    menu: MainMenu = MainMenu("BudgetBuddy")
    while (menu.get_state() != MainMenuState.CLOSING):
        try:
            menu.run()
        except (InvalidLoginCredentials) as e:
            print(e.message)


if __name__ == "__main__":
    main()
"""Program code"""

# Landon Lamie
# CIS 226
# 11/1/24

# First-party imports
from droids import DroidCollection
from userinterface import UserInterface


def main(*args):
    """Method to run program"""

    # Create a new instance of droid collection
    droid_collection = DroidCollection()

    # Create a new instance of the user interface
    user_interface = UserInterface(droid_collection)

    # Display greeting to user
    user_interface.display_greeting()

    # Display main menu and get choice from user
    choice = user_interface.get_menu_choice(3, user_interface.display_main_menu)

    # While the choice is not 3 (exit)
    while choice < 5:
        # If 1, create droid
        if choice == 1:
            user_interface.create_droid()
        # Else if 2, print list
        elif choice == 2:
            user_interface.print_droid_list()
        # Else if 3, sort by droid model (A, J, U, P)
        elif choice == 3:
            if not droid_collection.is_empty():
                droid_collection.sort_droids_type()
            user_interface.print_droid_list()
        # Else if 4, sort by total cost (least to most)
        elif choice == 4:
            if not droid_collection.is_empty():
                droid_collection.sort_by_total_cost()
            user_interface.print_droid_list()
        # Re-prompt for input
        choice = user_interface.get_menu_choice(5, user_interface.display_main_menu)

    # Display exiting program message.
    user_interface.display_exit_message()

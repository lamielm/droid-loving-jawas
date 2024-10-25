"""User Interface Module"""

# David Barnes
# CIS 226
# 6-4-2023

# First-party imports
from colors import (
    print_error,
    print_info,
    print_primary,
    print_success,
    print_warning,
)
from droids import (
    AstromechDroid,
    Droid,
    JanitorDroid,
    ProtocolDroid,
    UtilityDroid,
)


class UserInterface:
    """Do I/O with the user"""

    MAX_MENU_CHOICES = 5

    def __init__(self, droid_collection):
        """Constructor"""
        self.droid_collection = droid_collection

    def display_greeting(self):
        """Display the welcome greeting"""
        print()
        print_primary("Welcome to the Droid Inventory System")

    def display_main_menu(self):
        """Display the main menu"""
        print_info("What would you like to do?")
        print("1. Add a new droid to the system")
        print("2. Print the list of droids out")
        print("3. Sort Droids by Droid Model")
        print("4. Sort Droids by total cost (least $ to most $$$)")
        print("5. Exit the program")
        print()

    def display_exit_message(self):
        """Display the exit program message"""
        print_warning("Exiting the program. Thanks for using.")
        print()

    def print_droid_list(self):
        """Print the droid list out"""
        print()
        if self.droid_collection.is_empty():
            print_warning("The droid collection is currently empty.")
            print()
        else:
            print_success("This is the current droid list:")
            print(self.droid_collection)
            print()

    def create_droid(self):
        """Get new Droid info"""
        try:
            model_choice = self.get_menu_choice(5, self._display_model_selection_menu)
            material = self._get_material_selection()
            color = self._get_color_selection()

            if model_choice == 1:
                number_of_languages = self._get_language_selection()
                self.droid_collection.add_protocol(material, color, number_of_languages)
            elif model_choice in (2, 3, 4):
                toolbox, computer_connection, scanner = self._get_utility_options()
                if model_choice == 2:
                    self.droid_collection.add_utility(
                        material,
                        color,
                        toolbox,
                        computer_connection,
                        scanner,
                    )
                elif model_choice == 3:
                    broom, vacuum = self._get_janitor_options()
                    self.droid_collection.add_janitor(
                        material,
                        color,
                        toolbox,
                        computer_connection,
                        scanner,
                        broom,
                        vacuum,
                    )
                elif model_choice == 4:
                    navigation = self._get_option_selection("navigation")
                    number_of_ships = self._get_ship_selection()
                    self.droid_collection.add_astromech(
                        material,
                        color,
                        toolbox,
                        computer_connection,
                        scanner,
                        navigation,
                        number_of_ships,
                    )
        except CancelError:
            print()
            print_warning("Droid addition canceled.")
            print()
            return

    def get_menu_choice(self, max_choice, menu_function):
        """Prompt user for a menu choice"""
        menu_function()
        choice = self._get_int()
        while choice > max_choice:
            print_error("That is not a valid entry. Please enter a valid menu option.")
            menu_function()
            choice = self._get_int()
        return choice

    def _display_model_selection_menu(self):
        """Display model selection menu"""
        print_info("What type of droid is it?")
        print(f"1. {ProtocolDroid.model_name}")
        print(f"2. {UtilityDroid.model_name}")
        print(f"3. {JanitorDroid.model_name}")
        print(f"4. {AstromechDroid.model_name}")
        print("5. Cancel this operation")
        print()

    def _display_material_selection_menu(self):
        """Display material selection menu"""
        print_info("What material is the droid made out of?")
        print(f"1. {Droid.Materials.CARBONITE}")
        print(f"2. {Droid.Materials.VANADIUM}")
        print(f"3. {Droid.Materials.QUADRANIUM}")
        print(f"4. {Droid.Materials.TEARS_OF_A_JEDI}")
        print("5. Cancel this operation")
        print()

    def _get_material_selection(self):
        """Get the material selection"""
        int_choice = self.get_menu_choice(5, self._display_material_selection_menu)
        if int_choice == 1:
            choice = Droid.Materials.CARBONITE
        elif int_choice == 2:
            choice = Droid.Materials.VANADIUM
        elif int_choice == 3:
            choice = Droid.Materials.QUADRANIUM
        elif int_choice == 4:
            choice = Droid.Materials.TEARS_OF_A_JEDI
        else:
            raise CancelError
        return choice

    def _display_color_selection_menu(self):
        """Display color selection menu"""
        print_info("What color is the droid?")
        print(f"1. {Droid.Colors.WHITE}")
        print(f"2. {Droid.Colors.RED}")
        print(f"3. {Droid.Colors.GREEN}")
        print(f"4. {Droid.Colors.BLUE}")
        print("5. Cancel this operation")
        print()

    def _get_color_selection(self):
        """Get the color selection"""
        int_choice = self.get_menu_choice(5, self._display_color_selection_menu)
        if int_choice == 1:
            choice = Droid.Colors.WHITE
        elif int_choice == 2:
            choice = Droid.Colors.RED
        elif int_choice == 3:
            choice = Droid.Colors.GREEN
        elif int_choice == 4:
            choice = Droid.Colors.BLUE
        else:
            raise CancelError
        return choice

    def _get_language_selection(self):
        """Get number of languages droid knows"""
        return self._get_int(message="How many languages does the droid know?")

    def _get_ship_selection(self):
        """Get number of ships droid can interface with"""
        return self._get_int(message="How many ships can the droid interface with?")

    def _get_utility_options(self):
        """Get the utility droid options"""
        toolbox = self._get_option_selection("toolbox")
        computer_connection = self._get_option_selection("computer connection")
        scanner = self._get_option_selection("scanner")
        return toolbox, computer_connection, scanner

    def _get_janitor_options(self):
        """Get the janitor droid options"""
        broom = self._get_option_selection("broom")
        vacuum = self._get_option_selection("vacuum")
        return broom, vacuum

    def _get_option_selection(self, fieldname):
        """Get a bool option selection"""
        print_info(f"Does the droid have a {fieldname}? (y/n)")
        self._display_prompt()
        valid = False
        value = ""
        while not valid:
            user_input = input()
            if user_input.lower() == "y" or user_input.lower() == "n":
                valid = True
                value = user_input.lower() == "y"
            else:
                print_error("That is not a valid Entry.")
                print()
                print_info(f"Does the droid have a {fieldname}? (y/n)")
                self._display_prompt()
        return value

    def _display_prompt(self):
        """Display the input prompt"""
        print("> ", end="")

    def _get_int(self, message=None):
        """Get a valid int from the console."""
        if message:
            print_info(message)
        self._display_prompt()
        valid = False
        while not valid:
            try:
                value = int(input())
                # Ensure not negative.
                if value < 0:
                    raise ValueError

                valid = True
            except ValueError:
                print_error("That is not a valid Integer. Please enter a valid Integer.")
                if message:
                    print_info(message)
                self._display_prompt()
        return value


class CancelError(Exception):
    """Cancel Error Exception"""
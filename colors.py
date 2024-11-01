"""Console Color Helpers"""

# Landon Lamie
# CIS 226
# 11/1/24

# System imports
import os

os.system("")  # Required to get the terminal to ALWAYS show colors instead of raw escape codes.


# Decorator to convert Style class to a Singleton
def singleton(cls):
    """Singleton function"""
    return cls()


# Class of different Styles
@singleton
class Style:
    """Contains constants for colors"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    CLEAR = "\033[H\033[2J"

    def __getattribute__(self, name):
        """Override default dunder method"""
        value = super().__getattribute__(name)
        print(value, end="")
        return value


def print_success(message):
    """Print success message"""
    Style.GREEN  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_warning(message):
    """Print warning message"""
    Style.YELLOW  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_error(message):
    """Print error message"""
    Style.RED  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_primary(message):
    """Print primary message"""
    Style.BLUE  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_info(message):
    """Print info message"""
    Style.CYAN  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104

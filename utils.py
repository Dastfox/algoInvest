import os


def clear_console():
    """Clear the console."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

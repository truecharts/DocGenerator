from helpers import setup


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    CLEAN = '\033[0m'


def logger(message, color):
    if setup.VERBOSE:
        if color == "RED":
            print(Colors.RED + message)
        if color == "GREEN":
            print(Colors.GREEN + message)
        if color == "BLUE":
            print(Colors.BLUE + message)
        if color == "YELLOW":
            print(Colors.YELLOW + message)
        print(Colors.CLEAN)

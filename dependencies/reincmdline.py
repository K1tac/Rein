import os
from enum import Enum, auto

VERSION = "1.1.0"
DISTRIBUTION = "Rein Native"
AUTHOR = "K1tac"


class COMMANDLIST(Enum):
    HELP = auto()
    EXIT = auto()
    CLEAR = auto()
    VERSION = auto()
    AUTHOR = auto()
    DISTRIBUTION = auto()
    ABOUT = auto()
    LICENSE = auto()


class ReinCommand:
    def __init__(self, command: COMMANDLIST, description: str = ""):
        self.command = command
        self.description = description

    def execute(self, args: str = "") -> str:
        """Execute a command. Args is used for commands that take input."""
        if self.command == COMMANDLIST.HELP:
            return (
                "Available commands:\n"
                "help - Show this help message\n"
                "exit - Exit the command line interface\n"
                "clear - Clear the console\n"
                "version - Show the current version\n"
                "author - Show the author's name\n"
                "distribution - Show the distribution type\n"
                "about - Show information about Rein\n"
                "license - Show license information\n"
            )
        elif self.command == COMMANDLIST.EXIT:
            return "Exiting command line interface."
        elif self.command == COMMANDLIST.CLEAR:
            os.system("cls" if os.name == "nt" else "clear")
            return ""
        elif self.command == COMMANDLIST.VERSION:
            return f"Rein Version: {VERSION}"
        elif self.command == COMMANDLIST.AUTHOR:
            return f"Author: {AUTHOR}"
        elif self.command == COMMANDLIST.DISTRIBUTION:
            return f"Distribution: {DISTRIBUTION}"
        elif self.command == COMMANDLIST.ABOUT:
            return (
                f"{DISTRIBUTION} by {AUTHOR}\n"
                f"Version: {VERSION}\n"
                "Rein is a custom command line interface built in Python."
            )
        else:
            return "Unknown command."

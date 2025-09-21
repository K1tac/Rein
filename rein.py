import os
import time
import subprocess
from colorama import Fore, init
from dependencies.reincmdline import COMMANDLIST, ReinCommand

init(autoreset=True)

VERSION = "1.1.0"
DISTRIBUTION = "Rein Native"
AUTHOR = "K1tac"
USER = os.getlogin()
PATH = os.getcwd()

ASCII_BANNER = f"""
 /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
 /\_/\                                            /\_/\ 
( o.o )                                          ( o.o )
 > ^ <                                            > ^ < 
 /\_/\     .s5SSSs.  .s5SSSs.  s.  .s    s.       /\_/\ 
( o.o )          SS.       SS. SS.       SS.     ( o.o )
 > ^ <     sS    S%S sS    `:; S%S sSs.  S%S      > ^ < 
 /\_/\     SS    S%S SS        S%S SS`S. S%S      /\_/\ 
( o.o )    SS .sS;:' SSSs.     S%S SS `S.S%S     ( o.o )
 > ^ <     SS    ;,  SS        S%S SS  `sS%S      > ^ < 
 /\_/\     SS    `:; SS        `:; SS    `:;      /\_/\ 
( o.o )    SS    ;,. SS    ;,. ;,. SS    ;,.     ( o.o )
 > ^ <     `:    ;:' `:;;;;;:' ;:' :;    ;:'      > ^ < 
 /\_/\     {VERSION}                              /\_/\ 
( o.o )                                          ( o.o )
 > ^ <                                            > ^ < 
 /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
{DISTRIBUTION} by {AUTHOR}
"""

REQUIRED_PATHS = {
    "Rein/dependencies": "DEPENDENCIES DIRECTORY",
}

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def check_paths():
    """Ensure required paths exist, create if missing."""
    print("Checking for dependencies and necessary paths...\n")
    errors = 0
    for path, label in REQUIRED_PATHS.items():
        time.sleep(0.5)
        if not os.path.exists(path):
            print(f"{label} ... {Fore.YELLOW}MISSING{Fore.RESET}")
            try:
                os.makedirs(path, exist_ok=True)
                print(f"ISSUE {Fore.GREEN}RESOLVED{Fore.RESET} ~ CREATED {label}")
            except Exception as e:
                print(f"ISSUE {Fore.RED}FAILED{Fore.RESET} ~ {e}")
                errors += 1
        else:
            print(f"{label} ... {Fore.GREEN}OK{Fore.RESET}")
    return errors


def show_help():
    """Display help menu."""
    while True:
        print(
            """
        Help Menu
        [1] ~ Commands
        [2] ~ Creating your own Distro
        [0] ~ Back
        """
        )
        choice = input("Select an option: ")
        if choice == "1":
            print(ReinCommand(COMMANDLIST.HELP).execute())
        elif choice == "2":
            print(
                """
            Creating your own Distro:
            1. Fork the repository on GitHub.
            2. Clone your fork locally.
            3. Modify the code to create your own distribution.
            4. Test thoroughly before use.
            """
            )
        elif choice == "0":
            break
        else:
            print(f"{Fore.RED}Invalid option. Try again.{Fore.RESET}")


def rein_command_line():
    """Launch Rein's command line interface."""
    clear_console()
    print(ASCII_BANNER)
    print("Type 'exit' to return to the main menu.\n")

    while True:
        command = input(f"{USER}-[{PATH}]@rein:~# ").strip().lower()
        if not command:
            continue

        try:
            cmd_enum = COMMANDLIST[command.upper()]
            cmd_obj = ReinCommand(cmd_enum)
            output = cmd_obj.execute()
            if output:
                print(output)
            if cmd_enum == COMMANDLIST.EXIT:
                break
        except KeyError:
            try:
                result = subprocess.run(
                    command,
                    shell=True,
                    check=True,
                    text=True,
                    capture_output=True,
                )
                print(result.stdout)
                if result.stderr:
                    print(result.stderr, file=os.sys.stderr)
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Command failed:{Fore.RESET} {e.stderr}")


def main_menu():
    """Main menu loop."""
    while True:
        clear_console()
        print(ASCII_BANNER)
        print(
            """
        [1] ~ Rein Command Line
        [9] ~ Help
        [0] ~ Exit
        """
        )
        choice = input("Select an option: ")
        if choice == "1":
            rein_command_line()
        elif choice == "9":
            show_help()
        elif choice == "0":
            print("Exiting Rein...")
            break
        else:
            print(f"{Fore.RED}Invalid option. Try again.{Fore.RESET}")
            time.sleep(1)


def main():
    print("REIN ~ Booting\n")
    errors = check_paths()

    print("\nVersion:", VERSION)
    print("Distro:", DISTRIBUTION)
    print("Author:", AUTHOR)
    print()

    if errors == 0:
        print(f"{Fore.GREEN}Checks completed successfully!{Fore.RESET}")
        time.sleep(1)
        main_menu()
    else:
        print(f"{Fore.RED}Checks finished with {errors} errors.{Fore.RESET}")


if __name__ == "__main__":
    main()

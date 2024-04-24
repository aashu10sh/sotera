from rich.console import Console
from rich.markdown import Markdown


AVAILABLE_CHOICES: dict[int, str] = {
    1: "1. Login to your account",
    2: "2. Create a new account/register",
    3: "3. Quit the Program",
}


markdown = """
# Sotera - Fingerprint Based Autentication System!
## Built by Aashutosh Pudasaini - 1202

"""

for key, value in AVAILABLE_CHOICES.items():
    new = f"{value}\n"
    markdown += new


def print_navigation() -> None:
    console = Console()
    md = Markdown(markdown)
    console.print(md)


def get_user_choice() -> int:
    choice = 3
    try:
        choice = int(input("> "))
        if choice not in AVAILABLE_CHOICES.keys():
            raise ValueError
    except ValueError:
        print("Invalid Input")
        get_user_choice()
    return choice

"""
This file conatins the level structure
And the table that displays the levels and word count
for each level
It is then imported into run.py
"""
from colorama import Fore

level_table = {
    "E": ("Easy", "3 Letter words"),
    "M": ("Medium", "5 Letter words"),
    "H": ("Hard", "7 Letter words")
}


def display_level_table():
    """
    This function is for displaying a table for the level code,
    level type, and the word length of the level
    """
    print(f"{Fore.GREEN}| Code | Level  | Description        |")
    print("|------|--------|--------------------|")
    for code, (level, description) in level_table.items():
        print(f"|{Fore.GREEN}{code}     | {level:<6} | {description:<18} |")
    print(f"{Fore.GREEN}|------|--------|--------------------|")

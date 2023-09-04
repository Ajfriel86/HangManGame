"""
This is a file that contains the hangman
figure and is then imported into run.py
"""


def display_hangman(attempts):
    """
    This function displays the
    various stages of the hangman game
    based on the number of attempts left.
    """
    # This is the list of hangman stages
    hang = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\ |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\ |
       /    |
            |
        =========
        """,
        """
        +--+
        |   |
        O   |
       /|\\ |
       / \\ |
            |
        =========
        """
    ]

    # This displays/returns the hangman
    # figure based on the attempts taken
    return hang[6 - attempts]

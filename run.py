"""
Importing modules & files:
OS for clearing the screen
Random for generating random words
Colorama to add color to the text
Display files for hangman figure
Words files for the words for each level
Level files for the level structure
Level files for table displaying level structure
"""
import os
import random
from time import sleep
from colorama import Fore, Style
from display import display_hangman
from words import wordsDic
from level import level_table, display_level_table


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


class Hangman:
    """
    This is the definition of a new function, __init__ lets
    the class initialize the object's attributes
    self, is a reference to the instance of the object,
    while words & level are the values being passed when the
    instance is being created
    """

    def __init__(self, words, level):
        """
        This is the variable that stores
        the list of words,
        the level selected,
        the choosen word
        and guessed letters
        that are passed to the
        hangman game
        """
        self.words = words
        self.level = level
        self.word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 7

    def choose_word(self):
        """
        This function selects a random word from the
        array list of preselected words depending
        on the level selected
        By filtering the words and then
        selecting one at random
        """
        filtered_words = [
            word for word in self.words if len(word) == self.level]
        return random.choice(filtered_words)

    def display_guessed_letters(self):
        """
        This function is for displaying the
        guessed letters by a user
        """
        if self.guessed_letters:
            return "Guessed letters: " + ", ".join(self.guessed_letters)
        else:
            return ""

    def display_word(self):
        """
        This function is for generating a
        string that represents the word
        the user is trying to guess
        """
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def play(self):
        """
        This function is for the core logic of the game.
        It is responsible for the gameplay loop where
        the user guesses a letter from the hidden word
        """
        print(Fore.GREEN + "Welcome to Hangman!")
        print(Style.RESET_ALL)
        while True:
            print(
                Fore.GREEN + display_hangman(self.attempts) + Style.RESET_ALL)
            print(
                Fore.GREEN + self.display_word() + Style.RESET_ALL)
            print(
                Fore.BLUE + self.display_guessed_letters() + Style.RESET_ALL)
            try:
                guess = input(
                    f"""
                    {Fore.GREEN}Guess a letter:
                    """
                ).lower().strip()
                if len(guess) != 1 or not guess.isalpha():
                    raise ValueError(
                        f"""
                        {Fore.RED}Please enter a single letter only and
                        no numbers or special characters.
                        """ + Style.RESET_ALL
                    )
                if guess in self.guessed_letters:
                    raise ValueError(
                        f"""
                        {Fore.RED}You already guessed that letter.
                        Try another one.
                        """ + Style.RESET_ALL
                    )
                self.guessed_letters.append(guess)
                if guess in self.word:
                    print(
                        f"""
                        {Fore.GREEN}Correct! You got a letter!!
                        """ + Style.RESET_ALL
                    )
                else:
                    self.attempts -= 1
                    print(
                        f"""
                        {Fore.RED}
                        Wrong! You have {self.attempts} attempts left.
                        """ + Style.RESET_ALL
                    )
                if "_" not in self.display_word():
                    print(
                        f"""
                        {Fore.GREEN}Congratulations, you've guessed the word!
                        The word was :
                        """ + self.word + Style.RESET_ALL
                    )
                    sleep(2)
                    clear_screen()
                    break
                if self.attempts == 0:
                    print(
                        f"""
                        {Fore.RED}Sorry, you've run out of attempts.
                        The word was:
                        """ + self.word + Style.RESET_ALL
                    )
                    sleep(2)
                    clear_screen()
                    break
            except ValueError as e:
                print(f"{Fore.RED}{e}{Style.RESET_ALL}")

            sleep(5)
            clear_screen()
            continue
        while True:
            try:
                play_again = input(
                    f"""
                    {Fore.GREEN}Do you want to play again? (y/n):
                    """ + Style.RESET_ALL
                ).lower().strip()

                if play_again is None:
                    raise ValueError(f"""
                            {Fore.RED}Invalid input, please just select
                            y (Yes) or n (No).
                            """ + Style.RESET_ALL)

                play_again = play_again.lower().strip()

                if play_again == 'y':
                    return True
                elif play_again == 'n':
                    print(
                        f"{Fore.GREEN}Thank you for playing Hangman!")
                    return False
                else:
                    raise ValueError(
                        f"""
                            {Fore.RED}Invalid input, please just select
                            y (Yes) or n (No).
                            """ + Style.RESET_ALL +
                        sleep(2) +
                        clear_screen()
                    )
            except ValueError as e:
                print(f"{Fore.RED}{e}{Style.RESET_ALL}")


def main():
    """
    This is the main function of the Hangman game,
    handling the game setup, level selection, gameplay,
    and whether the user wants to play again.
    This is done through a loop that iterates through steps
    needed to play game.
    """

    while True:
        sleep(2)
        clear_screen()
        try:
            display_level_table()
            level_choice = input(
                "Choose a level (E for Easy, M for Medium, H for Hard): "
            ).upper().strip()

            if level_choice not in level_table:
                raise ValueError(
                    "Invalid selection. Please only select "
                    "'E' for Easy, 'M' for Medium, or 'H' for Hard.")

            chosen_level, _ = level_table[level_choice]
            print(f"You have chosen the '{chosen_level}' level.")

            if level_choice == "E":
                level_words = wordsDic["easy"]
                word_length = 3
            elif level_choice == "M":
                level_words = wordsDic["medium"]
                word_length = 5
            else:
                level_words = wordsDic["hard"]
                word_length = 7
            clear_screen()

            print(
                f"""
                    Instructions: You have 7 tries to guess a
                    {word_length}-letter word.
                    """
            )

            game = Hangman(level_words, word_length)
            play_again = game.play()
            if not play_again:
                print("Thanks for playing! Goodbye.")
                break

        except ValueError as e:
            print(f"{Fore.RED}{e}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()

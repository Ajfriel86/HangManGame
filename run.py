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
        This stores the list of words that are
        passed to the hangman game (object)
        """
        self.words = words
        # This stores the level selected
        self.level = level
        # Choose a random word of the level-selected
        self.word = self.choose_word()
        # This creates an empty list, when the user
        # guesses a letter it is added to the list
        self.guessed_letters = []
        # Number of attempts the user has
        self.attempts = 6

    def choose_word(self):
        """
        This function selects a random word from the
        array list of preselected words depending
        on the level selected
        """
        # This filters the words depending on
        # their length and then matches
        # that with the level selected
        filtered_words = [
            word for word in self.words if len(word) == self.level]

        # This returns a random word from the filtered words
        return random.choice(filtered_words)

    def display_guessed_letters(self):
        """
        This function is for displaying the guessed letters by a user
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
        # This is a loop that iterates through each letter
        for letter in self.word:
            # This checks if the letter selected is correct
            if letter in self.guessed_letters:
                # if it is correct it is displayed
                display += letter
            else:
                # If it is not correct the underscore remains
                display += "_"
        # This returns the word to be guessed with
        # underscores if it is incorrect
        return display

    def play(self):
        """
        This function is for the core logic of the game.
        It is responsible for the gameplay loop where
        the user guesses a letter from the hidden word
        """
        print("Welcome to Hangman!")

        # This is the gameplay loop that ensures
        # the game keeps playing until all
        # conditions are met
        while True:
            clear_screen()
            # Display the hangman figure
            print(display_hangman(self.attempts))
            # Display the letters when guessed correctly
            print("\n" + self.display_word())
            # This calls the function to display the
            # guessed letters by a user and prints it to screen
            print(self.display_guessed_letters())
            # This is a prompt for the user to input
            # a letter and store's the guessed letter
            # in the variable 'guess'
            guess = input("Guess a letter: ").lower().strip()

            # This if statement is for ensuring only
            # 1 letter was entered
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            # This if statement checks if a letter has
            # been selected already
            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            # If the letter selected meets the above criteria
            # it is added to the variable 'guess'
            self.guessed_letters.append(guess)

            # If the guessed letter is in the hidden word
            # - 'Correct!' - is displayed
            if guess in self.word:
                print("Correct!")
                # Else - Worg - and the number of attempts
                # left is displayed
            else:
                self.attempts -= 1
                print(f"Wrong! You have {self.attempts} attempts left.")

            # This if statement checks if all underscores
            # (hidden letters) have been guessed correctly
            # and if so, a congrats message is displayed
            if "_" not in self.display_word():
                print("Congratulations, you've guessed the word!")
                break

            # This if statement checks if the user
            # runs out of tries and displays a message
            # if they lost and the word they were trying
            # to guess
            if self.attempts == 0:
                print("Sorry, you've run out of attempts.\
                    The word was:", self.word)
                break

            # At the end of the
            # game a prompt is displayed to ask
            # the user if they wish to play again
            # or leave the game
        play_again = input(
            "Do you want to play again? (y/n): ").lower().strip()
        if play_again == 'y':
            return True
        else:
            print("Thank you for playing Hangman!")
            return False


def main():
    """
    This is the main function of the Hangman game,
    handling the game setup, level selection, gameplay,
    and whether the user wants to play again.
    """

    while True:  # This while loop is to keep the game running
        # This is to display the available levels
        # for the user to choose from
        display_level_table()
        # This is a prompt for the user to choose a level
        level_choice = input(
            "Choose a level code (E for Easy, M for Medium, H for Hard): "
        ).upper().strip()
        # This checks if the chosen level is valid
        if level_choice in level_table:
            # Validate the level choice so the user does not
            # input an incorrect value
            if level_choice not in {'E', 'M', 'H'}:
                print(
                    "Invalid level choice. Please enter 'E' \
                        for Easy, 'M' for Medium, or 'H' \
                        for Hard. No numbers, white space, \
                            or speicla charaters")
                continue
            # This gets the chosen level from the level_table
            chosen_level, _ = level_table[level_choice]
            # This displays the selected by the user
            print(f"You have chosen the '{chosen_level}' level.")
            # This is an if/elif statement to determine
            # the level selected by the user.
            # And checks if the chosen level is easy
            if level_choice == "E":
                # Selects the list of words for the easy level
                level_words = wordsDic["easy"]
                # Sets the word length for the easy level
                word_length = 3
                # Checks if the chosen level is medium
            elif level_choice == "M":
                # Selects the list of words for the medium-level
                level_words = wordsDic["medium"]
                # Sets the word length for the medium-level
                word_length = 5
                # If the chosen level is not easy or medium, it's hard
            else:
                # Selects the list of words for the hard-level
                level_words = wordsDic["hard"]
                # Sets the word length for the hard-level
                word_length = 7
            # Display game instructions
            print(
                f"Instructions: You have 6 tries to guess a \
                    {word_length}-letter word.")
            # Creates a Hangman game instance with
            # the chosen level's words and word length
            game = Hangman(level_words, word_length)
            # Starts playing the game and gets
            # whether the user wants to play again
            play_again = game.play()
            # Checks if the user doesn't want to play again
            if not play_again:
                # Displays a farewell message
                print("Thanks for playing! Goodbye.")
                # Exits the loop to end the game
                break
            # If the level selected is incorrect
        else:
            # Display an error message
            print("Invalid level choice.")


# This if statement ensures the main()
# function is executed when the script is run directly
if __name__ == "__main__":
    # Starts the main game loop if this script is run directly
    main()

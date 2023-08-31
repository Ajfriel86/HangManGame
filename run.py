# Import the random module for generating random words
import random


class Hangman:  # This is the class that defines the hangman game
    # this is a the definition of a new function, __init__ lets the class initialize the object's attributes, self, is a refrenece to the instance of the object, while words & level are the valuees being passed when the instance is being created
    def __init__(self, words, level):
        # This stores the list of words that are passed to the hangman game (object)
        self.words = words
        # This stores the level selected
        self.level = level
        # Choose a random word of the level selcted
        self.word = self.choose_word()
        #  This creates an empty list, when the user guesses a leeter it is added to the list
        self.guessed_letters = []
        # Number of attempts the user has
        self.attempts = 6

    # This function selects a random word from the array list of preselected words depending on the level selected
    def choose_word(self):
        # This filters the words depending on their length and then matchs that with the level selected
        filtered_words = [
            word for word in self.words if len(word) == self.level]
        # This returns a random word fropm the filtered words
        return random.choice(filtered_words)

    # This function is for generating a string that represents the word the user is trying to guess
    def display_word(self):
        # This initilizes an empty string
        display = ""
        # This is a loop that iterate through each letter
        for letter in self.word:
            # This checks if the letter selected is correct
            if letter in self.guessed_letters:
                # if it is correct it is displayed
                display += letter
            else:
                # If it is not correct the underscore remains
                display += "_"
        # This returns the word to be guessed with underscores fif it is inccorect
        return display

        # This functions displays the various stages of the hangman game
    def display_hangman(self):
        # This is the list of hangman stages
        hang = ["""
        
    +---+
    |   |
        |
        |
        |
        |
    =========""", """
    +---+
    |   |
    O   |
        |
        |
        |
    =========""", """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""", """
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========""", """
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========""", """
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========""", """
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    ========="""]
        # This dispalys/retunrs the hangman figure based on the attempts taken by the user
        return hang[6 - self.attempts]

    # This function is for the core logic of the game. It is responsible for the gameplay loop where the user guesses letter from the hidden word
    def play(self):
        # This is a text dispaly
        print("Welcome to Hangman!")

        # This is the gameplay loop that ensure the games keeps playing until all conditions are met
        while True:
            # Display the hangman figure
            print(self.display_hangman())
            # Display the letters when guessed correctly
            print("\n" + self.display_word())
            # This is a prompt for thr user to input a letter and stores the guessed letter in the varibale 'guess'
            guess = input("Guess a letter: ").lower()

            # This if statement is for ensuring only 1 letter was entered
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            # This if statement checks if a letter has been selected already
            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            # If the letter selected meets the above criteria it is added to the variable 'guess'
            self.guessed_letters.append(guess)

            # If the guessed letter is in the hidden word - 'Correct!' - is dispalyed
            if guess in self.word:
                print("Correct!")
                # Else - Worg - and the number of attempts left is displayed
            else:
                self.attempts -= 1
                print(f"Wrong! You have {self.attempts} attempts left.")

            # This if statement checks if all underscores (hidden letters) have been guessed correctly and if so, a congrats message is displayed
            if "_" not in self.display_word():
                print("Congratulations, you've guessed the word!")
                break

            # This if statement checks if the user runs out of tries and dispalys a message if they lsot and the word they were trying to guess
            if self.attempts == 0:
                print("Sorry, you've run out of attempts. The word was:", self.word)
                break

            # At the end of the game a prompt is displayed to ask the user if they wish to play again or leave the game
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            return True
        else:
            print("Thank you for playing Hangman!")
            return False


# Each level contains different word lengths and they are stored here
words = {
    "easy": ["cat", "dog", "bat", "hat", "pen"],
    "medium": ["apple", "banana", "cherry", "grape", "lemon"],
    "hard": ["elephant", "giraffe", "kangaroo", "zebra", "ostrich"]
}

# Each level is reffered to by its first letter and this corresponds to the level and word length for that level
level_table = {
    "E": ("Easy", "3 Letter words"),
    "M": ("Medium", "5 Letter words"),
    "H": ("Hard", "7 Letter words")
}


def display_level_table():  # This function is for displaying a table for the level code, level type, and the word length of the level
    print("| Code | Level  | Description        |")
    print("|------|--------|--------------------|")
    for code, (level, description) in level_table.items():
        print(f"| {code}    | {level:<6} | {description:<18} |")
    print("|------|--------|--------------------|")


def main():  # This is the main function of Hangman game, handling the game setup, level selection, gameplay, and whether the user wants to play again.
    # This while loop is to keep the game running
    while True:
        # This is to display the available levels for the user to choose from
        display_level_table()
        # This is a prompt for the user to choose a level
        level_choice = input(
            "Choose a level code (E for Easy, M for Medium, H for Hard): ").upper()
        # This checks if the chosen level selected is valid
        if level_choice in level_table:
            # This gets the chosen level from the level_table
            chosen_level, _ = level_table[level_choice]
            # This displays the selected by the user
            print(f"You have chosen the '{chosen_level}' level.")

            # This is an if/elif statement to determine the level selected by the user
            # Check if the chosen level is easy
            if level_choice == "E":
                # Selects the list of words for the easy level
                level_words = words["easy"]
                # Sets the word length for the easy level
                word_length = 3
            # Checks if the chosen level is medium
            elif level_choice == "M":
                # Selects the list of words for the medium level
                level_words = words["medium"]
                # Sets the word length for the medium level
                word_length = 5
                # If the chosen level is not easy or medium, it's hard
            else:
                # Selects the list of words for the hard level
                level_words = words["hard"]
                # Sets the word length for the hard level
                word_length = 7
            # Display game instructions
            print(
                f"Instructions: You have 6 tries to guess a {word_length}-letter word.")

            # Creates a Hangman game instance with the chosen level's words and word length
            game = Hangman(level_words, word_length)
            # Starts playing the game and gets whether the user wants to play again
            play_again = game.play()

            # Checks if the user doesn't want to play again
            if not play_again:
                # Displays a farewell message
                print("Thanks for playing! Goodbye.")
                # Exits the loop to end the game
                break
        # If the level selcted is incorrect
        else:
            # Display an error message
            print("Invalid level choice.")

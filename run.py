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

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

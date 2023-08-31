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

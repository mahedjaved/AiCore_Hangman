# %% Task 1 : Setup the Hangman class and the init functions
import random


class Hangman:
    def __init__(
            self,
            word,
            word_guessed,
            num_letters,
            word_list,
            list_of_guesses,
            num_lives=5,
    ):
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses
        self.num_lives = num_lives

        # set the word_guessed list as a list of '_' with same size as word string
        self.word_guessed = ['_' for i in range(len(self.word))]

        # store all the unique characters in the secret word into a list of unique characters
        unique_chars = list(set([word_ for word_ in word]))
        # pick from unique characters that are not in guessed list
        self.num_letters = len(
            [unique_char for unique_char in unique_chars if unique_char not in self.word_guessed])

        # A list of the guesses that have already been tried. Set this to an empty list initially
        self.list_of_guesses = []

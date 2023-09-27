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

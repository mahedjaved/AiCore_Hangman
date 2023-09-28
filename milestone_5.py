# %% Task 1 : Setup the Hangman class and the init functions
import random


class Hangman:
    def __init__(
            self,
            word_list,
            num_lives=5,
    ):
        self.word_list = word_list
        self.num_lives = num_lives
        # random pick from word list
        self.word = random.choice(self.word_list)
        # set the word_guessed list as a list of '_' with same size as word string
        self.word_guessed = ['_' for i in range(len(self.word))]
        # store all the unique characters in the secret word into a list of unique characters
        unique_chars = list(set([word_ for word_ in self.word]))
        # pick from unique characters that are not in guessed list
        self.num_letters = len(
            [unique_char for unique_char in unique_chars if unique_char not in self.word_guessed])
        # A list of the guesses that have already been tried. Set this to an empty list initially
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for word_idx, word in enumerate(self.word):
                if word == guess:
                    self.word_guessed[word_idx] = word

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_letters = self.num_letters - 1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Enter your guess: ")
            if (not guess.isalpha()) and (not len(guess) == 1):
                print(
                    "Invalid letter. Please, enter a single alphabetical character.")
            elif (guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
            if '_' not in self.word_guessed:
                break


def play_game(word_list):
    num_lives = 5
    game = Hangman(num_lives=num_lives, word_list=word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
        if game.num_lives > 0:
            game.ask_for_input()
        if game.num_lives != 0 and not game.num_letters > 0:
            print("Congratulations. You won the game!")


def __main__():
    play_game(['apple', 'bannanas'])

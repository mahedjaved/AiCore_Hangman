# %% Task 1: Iteratively check if the input is a valid guess

while (True):
    # ask the user for the input
    guess = input("Enter a single letter: ")

    # check if the input is alphabetic
    if guess.isalpha() and len(guess) == 1:
        print(f"Valid guess : {guess}")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# %% Task 2: Check whether the guess is in the word
!pip3 install random-word pyyaml
from random_word import RandomWords
secret_word = RandomWords().get_random_word().replace('-',' ')

# check if the input is alphabetic
if guess.isalpha() in secret_word:
    print(f"Good guess! {guess} is in the word.")
    
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


# %% Task 3: Check whether the guess is in the word
!pip3 install random-word pyyaml
from random_word import RandomWords
secret_word = RandomWords().get_random_word().replace('-',' ')

def check_guess(guess):
    """
    This function tests if guess entered is valid, considering the following
    cases: a) if it is alphabetical  b) if it is a single character  c) if it
    lies within the secret word chosen by the computer
    """
    guess = guess.lower()
    if guess.isalpha() and guess.lower() in secret_choice and len(guess) == 1:
        print(f"Good guess! {guess} is in the word.")
        return True
    
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False
    
def ask_for_input():
    """
    Ask the user for the input
    """
    return input("Enter a single letter: ")

while (True):
    guess = ask_for_input()
    if (check_guess(guess)):
        break


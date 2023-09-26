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
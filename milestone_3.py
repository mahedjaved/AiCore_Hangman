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

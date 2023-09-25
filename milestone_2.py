# %% Task -01

import random
word_list = ["Fr1", "Fr2", "Fr3", "Fr4", "Fr5"]
print(word_list)


# %% Task -02
word_list = ["Fr1", "Fr2", "Fr3", "Fr4", "Fr5"]
word = random.choice(word_list)
print(word)

# %% Task -03
guess = input("Enter a single letter: ")
# assert type(guess) == str and any(guess.lower() in string for string in ['abcdefghijklmnopqrstuvwxyz'])
if len(guess) == 1 and any(guess.lower() in string for string in ['abcdefghijklmnopqrstuvwxyz']):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
print(f"You have picked: {guess}")
# %%

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
assert type(guess) == str and guess.lower() in ['abcdefghijklmnopqrstuvwxyz']
print(f"You have picked: {guess}")
# %%

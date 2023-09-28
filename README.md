# Project Title - Hangman (AiCore)

Project aims to develop a digital clone of the popular word guessing game Hangman. The computer (in this eg) guesses a word and stores it in memory. It then iteratively asks whether the user guessed the word correctly or not.

# Project File Structure

Each of the milestones are devided into seperate .py files

(1) milestone_2.py : Basic draft code that checks a user's input and checks if the input is a single alphabet

(2) milestone_3.py : Develops code from milestone_2.py however make sure that if the user's input is invalid then continue asking via an infinite loop. Organises the user input request and guess checking in two seperate functions

(3) milestone_4.py : Develops code from milestone_3 and gives an OOP structure. The main class is termed Hangman, it contains two methods: a) check_guess b) ask_for_input.

(4) milestone_5.py : Builds on code from milestone_4.py and adds an external function that runs the Hangman class seperately

# Installation instructions

The .py files are further divided into seperate tasks that can run into seperate code cells in VSCode : https://code.visualstudio.com/docs/setup/windows

# Usage instructions

You can run any of the tasks as seperate cells in VSCode with Jupyter Notebook extensions installed

# License information

MIT License

# Special Cases

The following is used to special cases if

1. A '_' in the word :
   [Solution adopted] word.replace('_', ' ')

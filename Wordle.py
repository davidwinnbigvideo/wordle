# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        if s.upper() in FIVE_LETTER_WORDS:
            gw.show_message("Valid word")
        else:
            gw.show_message("Not a valid word")

    # Jan 12 David - function to display whatever word is passed
    def display_word(word):
        for col in range(N_COLS):
            gw.set_square_letter(0, col, word[col].upper())

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Jan 12 David - Fetches a random word from the list and calls the display_word function
    solution_word = random.choice(FIVE_LETTER_WORDS)
    display_word(solution_word)

# Startup code

if __name__ == "__main__":
    wordle()

# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    # Jan 18 Ethan - checks for valid word
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            # gw.show_message("Valid word")
            process_word(s.lower())
        else:
            gw.show_message("Not a valid word")

    def process_word(word):
        # Initialize variables to keep track of used letters
        used_letters = set()

        # Iterate through each column and compare letters
        for col in range(N_COLS):
            if word[col] == solution_word[col]:
                # Correct letter in correct position
                gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
            elif word[col] in solution_word and word[col] not in used_letters:
                # Correct letter but in the wrong position
                gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                used_letters.add(word[col])
            else:
                # Incorrect letter
                gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)

        # Update the current row
        gw.set_current_row(gw.get_current_row() + 1)

        # Check if all letters are correctly guessed
        if all(gw.get_square_color(gw.get_current_row() - 1, col) == CORRECT_COLOR for col in range(N_COLS)):
            gw.show_message("Congratulations! You guessed the word.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Jan 18 David - This was for mission 1
    # # Jan 12 David - function to display whatever word is passed
    # def display_word(word):
    #     for col in range(N_COLS):
    #         gw.set_square_letter(0, col, word[col].upper())
    # # Jan 12 David - Fetches a random word from the list and calls the display_word function
    solution_word = random.choice(FIVE_LETTER_WORDS)
    # display_word(solution_word)

# Startup code

if __name__ == "__main__":
    wordle()

# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Jan 18 Ethan - checks for valid word
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            
            process_word(s.lower())
        else:
            gw.show_message("Not a valid word")

    # Jan 24 David - Colors the images
    def process_word(word):
        used_letters = []
        row_count = 0
        correct_letters = []
        # Iterate through each column and compare letters
        for col in range(N_COLS):
            # Correct character if
            if word[col] == solution_word[col]:
                gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                correct_letters.append(word[col])
            # If there are duplicate charaters it handles it
            elif solution_word.count(word[col]) == 3 and word[col] not in used_letters and correct_letters.count(word[col]) == 3:
                gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                used_letters.append(word[col])
            elif solution_word.count(word[col]) == 2 and word[col] not in used_letters and correct_letters.count(word[col]) == 2:
                gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                used_letters.append(word[col])
            elif solution_word.count(word[col]) == 1 and word[col] not in used_letters and word[col] in correct_letters:
                gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                used_letters.append(word[col])
            # Wrong place, right character
            elif word[col] in solution_word and word[col] not in used_letters:
                gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                used_letters.append(word[col])
            # Wrong character
            else:
                gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)

        if all(gw.get_square_color(gw.get_current_row(), col) == CORRECT_COLOR for col in range(N_COLS)):
            gw.show_message("Congratulations! You guessed the word.")
            return
        row_count = row_count + 1
        if row_count < 6:
            gw.set_current_row(gw.get_current_row() + 1)

    def colorblind_popup():
        result = tk.messagebox.askquestion("Colorblind Mode", "Do you want to enable colorblind mode?")
        if result == 'yes':
            global CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
            CORRECT_COLOR = "#ADD8E6"
            PRESENT_COLOR = "#FFD700"
            MISSING_COLOR = "#999999"

    def run_colorblind_popup():
        t = Thread(target=colorblind_popup)
        t.start()
        t.join()
        
    # Creates game from our "mold"
    run_colorblind_popup()
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # solution_word = 'indie'
    solution_word = random.choice(FIVE_LETTER_WORDS)
    print(solution_word)

# Startup code

if __name__ == "__main__":
    wordle()

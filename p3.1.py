import streamlit as st
import random

# Hangman stages
HANGMAN_STATES = [
    "",  # 0 wrong
    " |----\n O   |\n     |\n     |\n     |\n     |\n-------",  # 1
    " |----\n O   |\n/    |\n     |\n     |\n     |\n-------",  # 2
    " |----\n O   |\n/|   |\n     |\n     |\n     |\n-------",  # 3
    " |----\n O   |\n/|\\  |\n     |\n     |\n     |\n-------",  # 4
    " |----\n O   |\n/|\\  |\n/    |\n     |\n     |\n-------",  # 5
    " |----\n O   |\n/|\\  |\n/ \\  |\n     |\n     |\n-------"  # 6
]

# Word list
WORDS = ["apple", "blanket", "bottle", "towel", "books", "paper", "kettle", "tablet", "mobile", "vinegar",
         "pillow", "greentea", "mirror", "school", "laptop"]

# Game initialization
def start_new_game():
    word = random.choice(WORDS)
    st.session_state.correct_word = word
    st.session_state.blank = ["_" for _ in word]
    st.session_state.wrong_count = 0
    st.session_state.guessed_letters = []
    st.session_state.game_over = False
    st.session_state.message = ""

# Game logic
def update_game_state():
    guess = st.session_state.guess_input.strip().lower()

    if not guess or len(guess) != 1 or not guess.isalpha():
        st.session_state.message = "Please enter a valid single letter."
        return

    if guess in st.session_state.guessed_letters:
        st.session_state.message = f"You already guessed '{guess}'."
        return

    st.session_state.guessed_letters.append(guess)

    if guess in st.session_state.correct_word:
        for i, letter in enumerate(st.session_state.correct_word):
            if letter == guess:
                st.session_state.blank[i] = guess
        if "_" not in st.session_state.blank:
            st.session_state.message = f"🎉 You won! The word was: {st.session_state.correct_word}"
            st.session_state.game_over = True
    else:
        st.session_state.wro_

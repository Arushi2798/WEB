import streamlit as st
import random

# Hangman ASCII art states
HANGMAN_STATES = [
    "",
    " |----\n O   |\n     |\n     |\n     |\n     |\n-------",
    " |----\n O   |\n/    |\n     |\n     |\n     |\n-------",
    " |----\n O   |\n/|   |\n     |\n     |\n     |\n-------",
    " |----\n O   |\n/|\\  |\n     |\n     |\n     |\n-------",
    " |----\n O   |\n/|\\  |\n/    |\n     |\n     |\n-------",
    " |----\n O   |\n/|\\  |\n/ \\  |\n     |\n     |\n-------"
]

WORDS = [
    "apple", "blanket", "bottle", "towel", "books", "paper", "kettle",
    "tablet", "mobile", "vinegar", "pillow", "greentea", "mirror", "school", "laptop"
]

def start_new_game():
    word = random.choice(WORDS)
    blank = ["_"] * len(word)
    st.session_state['correct_word'] = word
    st.session_state['blank'] = blank
    st.session_state['wrong_count'] = 0
    st.session_state['guessed_letters'] = []
    st.session_state['game_over'] = False
    st.session_state['message'] = ""

def update_game_state(guess):
    if st.session_state['game_over']:
        return

    guess = guess.lower()
    if not guess.isalpha() or len(guess) != 1:
        st.session_state['message'] = "Please enter a single alphabetic character."
        return

    if guess in st.session_state['guessed_letters']:
        st.session_state['message'] = f"You already guessed '{guess}'. Try a different letter."
        return

    st.session_state['guessed_letters'].append(guess)

    if guess in st.session_state['correct_word']:
        for i, char in enumerate(st.session_state['correct_word']):
            if char == guess:
                st.session_state['blank'][i] = guess
        st.session_state['message'] = f"Good guess! '{guess}' is in the word."
    else:
        st.session_state['wrong_count'] += 1
        st.session_state['message'] = f"Wrong guess! You have {6 - st.session_state['wrong_count']} guesses left."

    # Check win condition
    if "_" not in st.session_state['blank']:
        st.session_state['message'] = "🎉 YOU WON!! Congratulations!!!"
        st.session_state['game_over'] = True

    # Check lose condition
    if st.session_state['wrong_count'] >= 6:
        st.session_state['message'] = f"💀 GAME OVER! The correct word was: {st.session_state['correct_word']}"
        st.session_state['game_over'] = True

def main():
    st.title("Welcome to the HANGMAN Game!")

    if 'correct_word' not in st.session_state:
        start_new_game()

    st.text_area("Hangman figure:", value=HANGMAN_STATES[st.session_state['wrong_count']], height=150, max_chars=None, key=None)

    st.write("Word to guess:")
    st.write(" ".join(st.session_state['blank']))

    if not st.session_state['game_over']:
        guess = st.text_input("Guess a letter:", max_chars=1, key="guess_input")
        if st.button("Submit Guess"):
            update_game_state(guess)
            # Clear input after submit
            st.session_state['guess_input'] = ""

    st.write(st.session_state['message'])

    if st.session_state['game_over']:
        if st.button("Play Again"):
            start_new_game()
            st.experimental_rerun()


if __name__ == "__main__":
    main()

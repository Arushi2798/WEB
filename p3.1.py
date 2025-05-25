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
def update_game_state(guess):
    if not guess or len(guess) != 1 or not guess.isalpha():
        st.session_state.message = "Please enter a valid single letter."
        return

    guess = guess.lower()
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
        st.session_state.wrong_count += 1
        if st.session_state.wrong_count == 6:
            st.session_state.message = f"💀 Game Over! The word was: {st.session_state.correct_word}"
            st.session_state.game_over = True
        else:
            st.session_state.message = f"❌ Wrong guess! You have {6 - st.session_state.wrong_count} guesses left."

# Main UI
def main():
    # ✅ Lilac background using CSS
    st.markdown("""
        <style>
            body {
                background-color: #040404;
            }
            .stApp {
                background-color: #040404;
            }
        </style>
        """, unsafe_allow_html=True)

    st.title("🎮 Welcome to the HANGMAN Game!")

    if 'correct_word' not in st.session_state:
        start_new_game()
        st.rerun()


    # Show hangman drawing
    st.text_area("🪢 Hangman figure:", value=HANGMAN_STATES[st.session_state.wrong_count], height=150)

    # ✅ Show current state of word
    st.markdown("### 🔠 Word to guess:")
    st.markdown(f"### {' '.join(st.session_state.blank)}")

    if not st.session_state.game_over:
        guess = st.text_input("🔤 Guess a letter:", max_chars=1, key="guess_input")
        if st.button("Submit Guess"):
            update_game_state(guess)
            st.session_state["guess_input"] = ""  # Clear input
            st.rerun()


    st.markdown(f"**{st.session_state.message}**")

    if st.session_state.game_over:
        if st.button("🔁 Play Again"):
            start_new_game()
            st.rerun()


if __name__ == "__main__":
    main()

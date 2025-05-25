import streamlit as st
import random

st.title("🪨📄✂️ Rock Paper Scissors Game")
st.markdown("**Rules:** Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

choices = ["Rock", "Paper", "Scissors"]

user_choice = st.radio("Choose your move:", choices)

if st.button("Play!"):
    computer_choice = random.choice(choices)
    
    st.write(f"🤖 Computer chose: **{computer_choice}**")
    st.write(f"🧑 You chose: **{user_choice}**")

    if user_choice == computer_choice:
        st.success("It's a TIE!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.balloons()
        st.success("YOU WIN!")
    else:
        st.error("YOU LOSE!")

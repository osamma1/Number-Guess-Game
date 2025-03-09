import streamlit as st
import random

# Initialize game state
def initialize_game():
    if "number" not in st.session_state or st.session_state.reset:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.reset = False

def reset_game():
    st.session_state.reset = True
    initialize_game()

# Initialize game
initialize_game()

# Streamlit UI
st.title("🎯 Number Guessing Game By Usama Faraz")
st.markdown("<p style='color: #4CAF50; font-size: 18px;'>Can you find the hidden number? Test your guessing skills and challenge yourself! 🔢🔥</p>", unsafe_allow_html=True)

st.write("Guess the secret number between 1 and 100!")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write("🔵 Too low! Try again.")
    elif guess > st.session_state.number:
        st.write("🔴 Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!")
        st.session_state.game_over = True

if st.session_state.game_over:
    st.warning("Game Over! Press Reset to play again.")

if st.button("Reset Game"):
    reset_game()
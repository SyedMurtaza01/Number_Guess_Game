import streamlit as st
import random

def start_game():
   
    number_to_guess = random.randint(1, 100)
    return number_to_guess

def main():
   
    st.title("Number Guessing Game")

    min_value = st.number_input("Set minimum value:", min_value=1, value=1)
    max_value = st.number_input("Set maximum value:", min_value=1, value=100)

    difficulty = st.radio("Select difficulty", options=["Easy", "Medium", "Hard"])

    if difficulty == "Easy":
        max_attempts = 10
    elif difficulty == "Medium":
        max_attempts = 7
    else:
        max_attempts = 5

    if "number_to_guess" not in st.session_state:
        st.session_state.number_to_guess = start_game()

    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    guess = st.number_input(f"Guess a number between {min_value} and {max_value}:", min_value=min_value, max_value=max_value)

    if st.button("Guess"):
        if guess < st.session_state.number_to_guess:
            st.write("Too low!")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high!")
        else:
            st.write("Congratulations! You guessed it right!")
            st.session_state.number_to_guess = start_game()  

        st.session_state.attempts += 1

        st.write(f"Attempts: {st.session_state.attempts}")

        if st.session_state.attempts >= max_attempts:
            st.write(f"Game Over! The correct number was {st.session_state.number_to_guess}.")
            st.session_state.number_to_guess = start_game() 

    if st.button("Reset Game"):
        st.session_state.number_to_guess = start_game() 
        st.session_state.attempts = 0
        st.write("Game has been reset!")

if __name__ == "__main__":
    main()

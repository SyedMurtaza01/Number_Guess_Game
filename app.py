import streamlit as st
import random

# Function to start a new game
def start_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    return number_to_guess

# Set up the app
def main():
    # Display title
    st.title("Number Guessing Game")

    # Let the user set the custom range for the random number (Optional enhancement)
    min_value = st.number_input("Set minimum value:", min_value=1, value=1)
    max_value = st.number_input("Set maximum value:", min_value=1, value=100)

    # Set difficulty (Optional enhancement)
    difficulty = st.radio("Select difficulty", options=["Easy", "Medium", "Hard"])

    # Set number of attempts based on difficulty
    if difficulty == "Easy":
        max_attempts = 10
    elif difficulty == "Medium":
        max_attempts = 7
    else:
        max_attempts = 5

    # Store the generated random number
    if "number_to_guess" not in st.session_state:
        st.session_state.number_to_guess = start_game()

    # Store the attempt count
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    # Input field for user guess
    guess = st.number_input(f"Guess a number between {min_value} and {max_value}:", min_value=min_value, max_value=max_value)

    # Button to submit guess
    if st.button("Guess"):
        if guess < st.session_state.number_to_guess:
            st.write("Too low!")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high!")
        else:
            st.write("Congratulations! You guessed it right!")
            st.session_state.number_to_guess = start_game()  # Start a new game

        # Increase the number of attempts
        st.session_state.attempts += 1

        # Display the number of attempts
        st.write(f"Attempts: {st.session_state.attempts}")

        # Check if the game is over (out of attempts)
        if st.session_state.attempts >= max_attempts:
            st.write(f"Game Over! The correct number was {st.session_state.number_to_guess}.")
            st.session_state.number_to_guess = start_game()  # Start a new game

    # Button to reset the game
    if st.button("Reset Game"):
        st.session_state.number_to_guess = start_game()  # Start a new game
        st.session_state.attempts = 0
        st.write("Game has been reset!")

if __name__ == "__main__":
    main()

import random

def hangman_game():
    words = ["apple", "banana", "grape", "orange", "peach"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word_to_guess))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Display guessed state
        current_state = ""
        for letter in word_to_guess:
            current_state += (letter + " ") if letter in guessed_letters else "_ "

        print(current_state.strip())

        if "_" not in current_state:
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Game over! The word was: {word_to_guess}")

# Run the game
hangman_game()

# Prevent auto-close in some editors
input("Press Enter to exit...")

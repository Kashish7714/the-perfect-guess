import random


def get_valid_guess():
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            return guess
        except ValueError:
            print("Please enter a valid number.")


def play_game():
    """Run one round of the number guessing game."""
    secret = random.randint(1, 100)
    guesses = 0

    print("\n  Welcome to The Perfect Guess!")
    print("  I'm thinking of a number between 1 and 100.")
    print("  Let's see how many attempts it takes you.\n")

    while True:
        guess = get_valid_guess()
        guesses += 1

        if guess > secret:
            print("  Too high! Try a lower number.")
        elif guess < secret:
            print("  Too low! Try a higher number.")
        else:
            attempt_word = "attempt" if guesses == 1 else "attempts"
            print(f"\n  Correct! The number was {secret}.")
            print(f"  You got it in {guesses} {attempt_word}. Well played!\n")
            break


def main():
    while True:
        play_game()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing. See you next time!\n")
            break


if __name__ == "__main__":
    main()

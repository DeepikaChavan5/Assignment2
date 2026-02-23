import random

best_score = None  # Track minimum attempts

while True:
    number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0
    guessed_correctly = False

    print("\n=== NUMBER GUESSING GAME ===")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it!")

    while attempts_left > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("⚠ Please enter a number between 1 and 100!")
                continue

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        attempts_used += 1
        attempts_left -= 1

        if guess == number:
            print(f"Congratulations! You guessed it in {attempts_used} attempts.")
            guessed_correctly = True

            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print("New Best Score!")

            break

        elif guess > number:
            print("Too High!")
        else:
            print("Too Low!")

        # Bonus hint (within 5)
        if abs(guess - number) <= 5:
            print("Very Close!")

        print(f"Attempts remaining: {attempts_left}")

    if not guessed_correctly:
        print(f"\nGame Over! The correct number was {number}.")

    if best_score is not None:
        print(f"Best Score: {best_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
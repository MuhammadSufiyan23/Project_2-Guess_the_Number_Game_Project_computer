# PROJECT: 2

# GUESS THE NUMBER GAME PYTHON PROJECT (Computer)

import random

def main():
    random_number = random.randint(1, 99)
    attempts = 0

    print("🤖 I am thinking of a number between 1 and 99...")
    print("🔢 Try to guess the number! (Type 'q' to quit)")

    while True:
        guess = input("🎯 Enter your guess: ")

        if guess.lower() == 'q':  
            print("🚪 Exiting the game. Better luck next time! 👋")
            break

        try:
            guess = int(guess)
            attempts += 1

            if guess < random_number:
                print("📉 Your guess is too low! Try again. ⬆️")
            elif guess > random_number:
                print("📈 Your guess is too high! Try again. ⬇️")
            else:
                print(f"🎉 Congrats! The number was {random_number}. 🏆")
                print(f"🔢 You guessed it in {attempts} attempts! 🎯")
                print("🙏 Thank you for playing!")
                break  
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1 and 99.")

main()

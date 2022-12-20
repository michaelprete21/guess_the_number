from art import logo
import random

g_number = random.randint(1,100)

def guessing_game():
    """Code for the guessing game"""
    print(logo)
    print("\nI'm thinking of a number between 1 and 100.\n")
    print(f"The number is {g_number}")
    difficulty = input("Choose a difficulty between 'easy' or 'hard': ")

    while True:
        if difficulty == 'easy':
            countdown = 10
            break
        elif difficulty == 'hard':
            countdown = 5
            break
        else:
            print("Please enter a valid response.")
            continue

    while countdown != 0:
        print(f"You have {countdown} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > g_number:
            print("You are too high")
            countdown -= 1
        elif guess < g_number:
            print("You are too low")
            countdown -= 1
        elif guess == g_number:
            print("You win!")
            break

    if countdown == 0:
        print("You lose!")

guessing_game()

continuation = input("Would you like to continue? Yes or No ").lower()

if continuation == "yes":
    guessing_game()

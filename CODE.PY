import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct! You guessed it right.")
else:
    print(f" Wrong! The correct number was {secret_number}.")

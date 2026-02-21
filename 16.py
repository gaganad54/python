


import random

number = random.randint(1, 100)
attempts = 7

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
# checking the gueses
    if guess == number:
        print("🎉 Congratulations! You guessed correctly.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    print("Attempts left:", attempts - attempt)

else:
    print(" Game Over! The number was:", number)
import random
number = random.randint(1, 50)
attempts = 0
print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 50")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Correct! You won!")
        print("Attempts:", attempts)
        break

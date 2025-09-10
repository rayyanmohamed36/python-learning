import random

secretnumber = random.randint(1, 100)

print("Welcome to the Number Guessing Game")
print("Guess a number between 1 and 100.")

attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secretnumber:
        print("Too low! Try again.")
    elif guess > secretnumber:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secretnumber} in {attempts} attempts.")
        break

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100
import random
secret_number = random.randint(1, 100)

# Ask the user to choose a difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Set the number of attempts based on the difficulty level
if difficulty == "easy":
	attempts = 10
else:
	attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

# Keep track of the number of guesses
guesses = 0

# Loop until the user guesses the number or runs out of attempts
while guesses < attempts:
	guess = int(input("Guess a number between 1 and 100: "))
	guesses += 1
	print(f"You have {attempts - guesses} attempts remaining to guess the number.")
	if guess == secret_number:
		print(f"You got it! The answer was {secret_number}.")
		print(f"You guessed the number in {guesses} tries.")
		break
	elif guess < secret_number:
		print("Too low. Guess again.")
	else:
		print("Too high. Guess again.")

# If the user runs out of attempts, print the correct answer
if guesses == attempts:
	print(f"You lose. The correct answer was {secret_number}.")




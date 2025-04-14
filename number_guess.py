# All Libraries Installed :- 
import random

# Setting The Range Of The Game :- 
lower_bound = int(input("Set The Lowest Number :- "))
upper_bound = int(input("Set The Highest Number :- "))

# Generating A Random Number Between The Range :- 
target_number = random.randint(lower_bound, upper_bound)

# Number of Attempts :- 
attempts = 0

# Displaying The Virtual Interface :- 
print("Welcome to the Number Guessing Game! I'm thinking of a number between",(lower_bound),"and",(upper_bound),"..Try to guess it!")

while True:
    # Getting What The User Guesses :- 
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Checking  if the Guess is Correct or Not :- 
    if guess < target_number:
        print("Thsi Is Too low! Try again.")
    elif guess > target_number:
        print("This Is Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number",(target_number),"in" ,(attempts),"attempts.")
        print("Thank You . It was a Good Game.")
        break

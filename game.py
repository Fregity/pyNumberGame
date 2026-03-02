import random

def getNumber():
    return random.randint(1, 100)

if __name__ == "__main__":
    number = getNumber()
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    print("Each round, you will be prompted to enter your guess. After each guess, I will tell you if your guess is too low, too high, or correct.")
    print("You can choose a difficulty level to determine how many attempts you have.")
    print("Easy: 10 attempts, Medium: 5 attempts, Hard: 3 attempts")
    difficulty = input("Choose difficulty (Easy, Medium, Hard): ").lower()
    if difficulty == "easy" or difficulty == "e":
        attemptsLeft = 10
    elif difficulty == "medium" or difficulty == "m":
        attemptsLeft = 5
    elif difficulty == "hard" or difficulty == "h":
        attemptsLeft = 3
    else:
        print("Invalid difficulty level. Defaulting to medium.")
        attemptsLeft = 5
    while attemptsLeft > 0:
        try:
            guess = int(input("Enter your guess: "))
            attemptsLeft -= 1
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts and had {attemptsLeft} attempts left!")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
    else:
        print(f"Game over! You've used all your attempts. The number was {number}.")


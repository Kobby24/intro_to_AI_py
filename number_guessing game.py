import random

print("Welcome to Number Guessing Goal!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
num_guessesd = random.randint(1,100)

def easy():
    attempts = 10
    print(f"You have {attempts} attempts ")
    guess = int(input("Make a guess: "))
    
    
    while guess != num_guessesd:
        if guess > num_guessesd:
            attempts -= 1
            print("Too high")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
            
        elif guess < num_guessesd:
            attempts -= 1
            print("Too low")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
            
        if attempts == 0:
            print("Game over")
            return 0
        guess = int(input("Make a guess: "))
        if guess == num_guessesd:
            print(f"You got it the answer was {num_guessesd}")
def hard():
    attempts = 5
    print(f"You have {attempts} attempts ")
    guess = int(input("Make a guess: "))
    
    
    while guess != num_guessesd:
        if guess > num_guessesd:
            attempts -= 1
            print("Too high")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
            # guess = int(input("Make a guess: "))
        elif guess < num_guessesd:
            attempts -= 1
            print("Too low")
            print("Guess again")
            print(f"You have {attempts} remaining to guess the number.")
            
        if attempts == 0:
            print("Game over")
            return 0
        guess = int(input("Make a guess: "))
        if guess == num_guessesd:
            print(f"You got it the answer was {num_guessesd}")
if difficulty == "easy":
    easy()
elif difficulty == "hard":
    hard()
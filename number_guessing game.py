import random

print("Welcome to Number Guessing Goal!\nI am thinking of a number between 1 and 100.")
play = True


def cont():
    not_made_decision = True
    while not_made_decision:

        decision = input('Do want to play again\n1.Yes\n2.No\n')
        if decision.strip() == '1':

            return True
        elif decision.strip() == '2':

            return False
        else:
            print('\n\nInvalid input! Enter a number 1 or 2\n')


def error(num1, num2):
    print(f'Invalid Input! Enter a number between {num1} and {num2}')


while play:

    difficulty = input(
        "Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) "
        "\n3. Hard (3 chances) \n\nEnter your choice: ")
    numb_guessed = random.randint(1, 100)


    def play(level, num: int):

        level = level
        gone = 0

        if level.strip() == '1':
            attempts = 10
            print(f"Great! You have selected the Easy difficulty level.\nLet's start the game!\n\n")
        elif level.strip() == "2":
            attempts = 5
            print(f"Great! You have selected the Medium difficulty level.\nLet's start the game!\n\n")
        elif level.strip() == "3":
            attempts = 3

            print(f"Great! You have selected the Hard difficulty level.\nLet's start the game!\n\n")
        else:
            error(1, 3)
            return 0
        print(num)

        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                error(1, 100)
            else:
                if guess > 0:
                    if guess > num:
                        attempts -= 1
                        gone += 1
                        print("Too high")
                        print("Guess again")
                        print(f"You have {attempts} attempts remaining to guess the number.\n\n")

                    elif guess < num:
                        attempts -= 1
                        gone += 1
                        print("Too low")
                        print("Guess again")
                        print(f"You have {attempts} attempts remaining to guess the number.\n\n")
                    if attempts == 0:
                        print("Game over\n\n")
                        return 0

                    if guess == num:
                        gone += 1
                        print(f"You guessed the number in {gone} attempts\n\n")

                        return 0
                else:
                    error(1, 100)


    play(difficulty, numb_guessed)
    if cont():
        play = True
    else:
        play = False

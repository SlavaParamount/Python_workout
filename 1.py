from random import randint

def guessing_game():
    number = randint(0, 100)

    print("Guess a number (0 to 100):")

    while True:
        number_input = int(input())

        if number_input == number:
            print("You right!!")
            break

        elif number_input < number:
            print("Too low")

        elif number_input > number:
            print("Too high")

guessing_game()

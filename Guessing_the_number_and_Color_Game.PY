import random


def random_color():
    colors = ['red', 'green', 'blue']
    secret_color = random.choice(colors)

    print("Welcome to the Game!")
    print("Guess the Color:"
          "1.Red"
          "2.Green"
          "3.Blue")

    while True:

        guess = input("Enter the Color Name (Type 'quit' to exit)").strip().lower()

        if guess == 'quit':
            print(f"Thank you for playing! color was {secret_color}")
            break

        if guess not in colors:
            print("Please enter a valid color")
            continue

        if guess == secret_color:
            print(f"Guess is Correct! color is {secret_color}")
            break
        else:
            print("Guess is Incorrect!")


def guess_the_number():
    print("Welcome to the game!")
    print("I am thinking of a number between 1 and 10.")
    secret_number = random.randint(1, 10)

    attempts = 0
    while True:

        guess = input("Guess a number (Type 'quit' to exit): ").strip().lower()

        if guess == 'quit':
            print(f"Thanks For Playing,The number was {secret_number}")
            break
        try:
            guess = int(guess)
            if guess < 1 or guess > 10:
                print("Sorry, guess between 1 and 10")
                continue

            if guess < secret_number:
                print("Guess is low")
            elif guess > secret_number:
                print("Guess is high")
            else:
                print("Congrats! Guess is Correct")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    print("1.Color Guess Game")
    print("2.Number Guess Game")
    x = input("Choose your Game:-")

    if x == '1':
        random_color()
    elif x == '2':
        guess_the_number()
    else:
        print("Enter the Valid Number.")


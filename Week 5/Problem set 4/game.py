import random

def main():
    level = get_int("Level: ")
    number = random.randint(1,level)
    while True:
        guess = get_int("Guess: ")
        if number > guess:
            print("Too small!")
        elif number < guess:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_int(str):
    while True:
        try:
            value = int(input(str))
            if value > 0:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()

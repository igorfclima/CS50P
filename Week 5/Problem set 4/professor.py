from random import randint


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    # Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    # Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+)


    # Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again

if __name__ == "__main__":
    main()

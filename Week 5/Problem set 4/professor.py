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
    x_numbers = []
    y_numbers = []
    results = []

    for i in range(10):
        if level == 1:
            x = randint(0,9)
            y = randint(0,9)
        elif level == 2:
            x = randint(10,99)
            y = randint(10,99)
        else:
            x = randint(100,999)
            y = randint(100,999)
        x_numbers.append(x)
        y_numbers.append(y)
        results.append(x + y)
    # Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again
    for i in range(len(results)):
        points = 0
        while True:
            guess = int(input(f"{x_numbers[i]} + {y_numbers[i]} = "))

            if guess == results[i]:
                points += 1
                break
            else:
                print("EEE")
        if i == 10:
            print(f"Score: {points}")


if __name__ == "__main__":
    main()

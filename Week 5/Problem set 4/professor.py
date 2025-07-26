from random import randint


def main():
    level = get_level()
    score = 0
    num_problems = 10
    for _ in range(num_problems):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        attemps = 0
        while attemps  < 3:
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attemps += 1
            except ValueError:
                print("EEE")
                attempts += 1
        else:
            print(f"{x} + {y} = {correct_answer}")
    print(f"Score: {score}")


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
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    elif level == 3:
        return randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()

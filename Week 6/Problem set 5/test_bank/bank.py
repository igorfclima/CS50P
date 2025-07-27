def main():
    greeting = input("Greeting: ")
    cents = value(greeting)
    print(f"{cents}")


def value(greeting):
    if greeting.lower().startswith("hello"):
        return "$0"
    elif greeting.lower().startswith("h"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()

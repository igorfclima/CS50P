def main():
    greeting = input("Greeting: ")
    cents = value(greeting)
    print(f"${cents}")


def value(greeting):
    normalize_greeting = greeting.strip().lower()

    if normalize_greeting.startswith("hello"):
        return 0
    elif normalize_greeting.startswith("h"):
        return 20
    else: return 100


if __name__ == "__main__":
    main()

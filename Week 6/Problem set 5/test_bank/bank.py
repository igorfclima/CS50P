def main():
    greeting = input("Greeting:")
    cents = value(greeting)
    print(f"${cents}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

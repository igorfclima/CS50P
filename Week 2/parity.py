def main():
    x = int(input("Tell me a number: "))
    if isEven(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

def isEven(number):
    return number % 2 == 0

main()

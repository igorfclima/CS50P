def main():
    number = int(input("Tell me a number: "))
    print(f"The squareroot of {number} is {square(number)}")

def square(num):
    return pow(num,2)

main()

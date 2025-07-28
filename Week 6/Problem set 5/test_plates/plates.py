def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    if not (2 <= len(str) <= 6):
        return False
    if not str[0:2].isalpha():
        return False
    if not str.isalnum():
        return False
    found_number = False
    for i in range(len(str)):
        if str[i].isdigit():
            if not found_number and str[i] == '0':
                return False
            found_number = True
            if not str[i:].isdigit():
                return False
            break
    return True


if __name__  == "__main__":
    main()

def main():
    print(f"Output: {shorten(input("Input: "))}")


def shorten(word):
    vowels = ["a","e","i","o","u"]
    shortened = ""
    for char in word:
        if not char.lower() in vowels:
            shortened += char
    return shortened



if __name__ == "__main__":
    main()

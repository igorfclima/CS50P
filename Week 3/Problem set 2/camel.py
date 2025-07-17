def main():
    camel_case_input = input("camelCase: ").strip()
    print(string_converter(camel_case_input))

def string_converter(text):
    snake_case = ""
    for char in text:
        if char.isupper():
            snake_case += ("_" + char.lower())
        else:
            snake_case += char.lower()
    return snake_case

if __name__ == "__main__":
    main()

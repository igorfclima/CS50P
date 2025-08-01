import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")
    code_lines = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                striped_line = line.strip()
                if striped_line and not striped_line.startswith("#"):
                    code_lines += 1
        print(code_lines)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

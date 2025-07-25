import sys
import inflect #type: ignore

def main():
    p = inflect.engine()
    name_list = []

    while True:
        try:
            name = input("Name: ").strip()
            if name:
                name_list.append(name)

        except EOFError:
            print()
            break

    if not name_list:
        sys.exit(0)

    final_names_string = p.join(name_list)

    print(f"Adieu, adieu, to {final_names_string}")

if __name__ == "__main__":
    main()

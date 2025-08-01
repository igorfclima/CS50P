import sys
import csv
from tabulate import tabulate #type: ignore

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")


    try:
        pizzas_data = []
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                try:
                    pizza_name = row[0]
                    small_price_str = row[1]
                    large_price_str = row[2]

                    small_price = float(small_price_str.replace('$', ''))
                    large_price = float(large_price_str.replace('$', ''))

                except (ValueError, IndexError):
                    sys.exit(f"Invalid data format in row: {row}. Expected Name, $Small, $Large.")

                pizzas_data.append({
                    "name": pizza_name,
                    "small": small_price,
                    "large": large_price
                })

    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"An unexpected error occurred while reading the file: {e}")

    headers = ["Pizza", "Small", "Large"]
    formatted_rows = []
    for pizza in pizzas_data:
        formatted_rows.append([
            pizza["name"],
            f"${pizza['small']:.2f}",
            f"${pizza['large']:.2f}"
        ])

    print(tabulate(formatted_rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()

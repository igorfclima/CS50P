import sys
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")
    #elif not (file_name.startswith("regular") or file_name.startswith("sicilian")):
        #sys.exit("Not a CSV file")
    try:
        pizzas = []
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    pizza_name = row["name"]
                    small_price = float(row["small"])
                    large_price = float(row["large"])
                except ValueError:
                    sys.exit(f"Invalid price format in row for {row.get('name', 'unknown pizza')}")
                except KeyError as e:
                    sys.exit(f"Missing column in CSV: {e}. Expected 'name', 'small', 'large'. ")
                pizzas.append({
                    "name": pizza_name,
                    "small": small_price,
                    "large": large_price
                })
    except FileNotFoundError:
        sys.exit("File does not exist")

    if sys.argv[1] == "regular.csv":
        headers = ["Regular Pizza", "Small", "Large"]
    else:
        headers = ["Sicilian Pizza", "Small", "Large"]

    formatted_rows = []
    for pizza in pizzas:
        formatted_rows.append([
            pizza["name"],
            f"${pizza['small']:.2f}",
            f"${pizza['large']:.2f}"
        ])

    print(tabulate(formatted_rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()

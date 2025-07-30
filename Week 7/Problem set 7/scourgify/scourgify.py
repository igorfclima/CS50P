import csv
import sys

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]


    if not input_file_name.endswith(".csv"):
        sys.exit("Input file is not a CSV file")
    if not output_file_name.endswith(".csv"):
        sys.exit("Output file is not a CSV file")

    scourgify_csv(input_file_name, output_file_name)

def scourgify_csv(input_file_path, output_file_path):
    transformed_data = []

    try:
        with open(input_file_path, "r", newline='') as infile:
            reader = csv.DictReader(infile)
            if "name" not in reader.fieldnames or "house" not in reader.fieldnames:
                sys.exit("Input CSV missing 'name' or 'house' columns.")

            for row in reader:
                try:
                    full_name = row["name"]
                    house = row["house"]

                    name_parts = full_name.split(",")
                    if not len(full_name) > 2:
                        sys.exit()
                    first = name_parts[1].strip()
                    last = name_parts[0].strip()

                    transformed_data.append({
                        "first": first,
                        "last": last,
                        "house": house
                    })
                except IndexError:
                    sys.exit()
    except FileNotFoundError:
        sys.exit()

    try:
        fieldnames = ["first", "last", "house"]
        with open(output_file_path, "w", newline='') as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(transformed_data)
    except IOError as e:
        sys.exit(f"Could not write to {output_file_path}: {e}")
    except Exception as e:
        sys.exit(f"An unexpected error occurred during writing to '{output_file_path}': {e}")

if __name__ == "__main__":
    main()

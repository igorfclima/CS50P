def main():
    while True:
        fuel_str = input("Fraction: ").strip()
        try:

            fraction_float = convert(fuel_str)

            print(gauge(fraction_float))
            break
        except (ValueError, ZeroDivisionError):

            pass

def convert(fraction_str):

    parts = fraction_str.split("/")

    if len(parts) != 2:
        raise ValueError

    try:
        numerator = int(parts[0])
        denominator = int(parts[1])
    except ValueError:
        raise ValueError

    if denominator == 0:
        raise ZeroDivisionError

    if numerator > denominator:
        raise ValueError
    return numerator / denominator

def gauge(percentage_float):
    rounded_percentage = round(percentage_float * 100)

    if rounded_percentage <= 10:
        return "E"
    elif rounded_percentage >= 90:
        return "F"
    else:
        return f"{rounded_percentage}%"

if __name__ == "__main__":
    main()

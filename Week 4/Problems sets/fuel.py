def calc_fraction():
    fuel = input("Fraction: ").strip().lower()
    try:
        parts = fuel.split('/')
        first_fraction = int(parts[0])
        second_fraction = int(parts[1])
        fraction = first_fraction / second_fraction

        if 0 <= fraction <= 1:
            if fraction > 0.9:
                return "F"
            elif fraction < 0.10 > 0:
                return "E"
            else:
                return f"{round(fraction * 100)}%"
        else:
            calc_fraction()

    except (ValueError, ZeroDivisionError, IndexError):
        calc_fraction()

print(calc_fraction())

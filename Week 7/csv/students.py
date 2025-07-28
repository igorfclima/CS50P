with open("Week 7/csv/names.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

import csv

students = []

with open("Week 7/csv/names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is from {student['home']}")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier "},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(f"Name: {student["name"]}, House: {student["house"]}")

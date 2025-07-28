import csv

name = input("What is your name: ")
home = input("Where is your home: ")

with open("Week 7/csv w/names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})

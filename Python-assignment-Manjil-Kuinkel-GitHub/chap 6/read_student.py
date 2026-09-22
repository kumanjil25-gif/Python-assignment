import csv

with open("student.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for student in reader:
        student = {key.strip(): value.strip() for key, value in student.items()}

        print("Roll No:", student["Roll No"])
        print("Name:", student["Name"])
        print("Address:", student["Address"])
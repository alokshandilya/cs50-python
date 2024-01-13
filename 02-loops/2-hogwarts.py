# Demonstrates indexing into a list
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

print("#######")

# Demonstrates iterating over a list
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

print("#######")

# Demonstrates iterating over and indexing into a list
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

print("#######")

# Demonstrates indexing into a dict
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("#######")

# Demonstrates iterating over and index into a dict
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

print("#######")

# Demonstrates iterating over a list of dict objects
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

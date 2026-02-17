students = {
    "katlego": 80,
    "jermaine": 75,
    "kendrick": 85,
    "drake": 70
}

print("student records")

for name, grade in students.items():
    print(f"{name}: {grade}")

new_student = input("enter the students name: ")
new_grade = input("enter the students grade: ")

students[new_student] = new_grade

print("update records")
for name, grade in students.items():
    print(f"{name}: {grade}")

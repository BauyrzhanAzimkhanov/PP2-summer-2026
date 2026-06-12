student_marks = dict({"Dana": "A", "Aruna": "A-", "Sundet": "B+", "Nurbol": "F"})

student_marks.update({"Aruzhan": "C+"})
student_marks.update({"Aruzhan": "B"})
student_marks["Aruzhan"] = "B"
student_marks["Bool"] = True
student_marks["Float"] = 76.5
student_marks["List"] = [1, 2]
student_marks["Set"] = set(("test", "test1"))
student_marks["Dict"] = dict({"Hello": "World"})
print(student_marks)

for k, v in student_marks.items():
    print("Key:", k, "Value:", v)

cars = ["Toyota", "Honda", "Suzuki"]

for k, v in enumerate(cars):
    print("Key:", k, "Value:", v)

clubs = tuple(("Braca", "Atleti", "Villareal", False, 14.88, -94))
for k, v in enumerate(clubs):
    print("Key:", k, "Value:", v)

subjects = {"Calculus", "PE", "Arts", "Differential math", "Physics"}
for k, v in enumerate(subjects):
    print("Key:", k, "Value:", v)
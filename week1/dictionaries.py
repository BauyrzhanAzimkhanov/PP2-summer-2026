student_marks = dict({"Dana": "A", "Aruna": "A-", "Sundet": "B+", "Nurbol": "F"})
# student_marks = {"Dana": "A", "Aruna": "A-", "Sundet": "B+", "Nurbol": "F"}
for mark in student_marks:
    print(mark)
print(student_marks)
for k, v in student_marks.items():
    print("Key:", k, "Value:", v)
student_marks.update({"Aruzhan": "C+"})
print(student_marks)
student_marks.update({"Aruzhan": "B"})
student_marks["Aruzhan"] = "B"
print(student_marks)
student_marks["Bool"] = True
student_marks["Float"] = 76.5
student_marks["List"] = [1, 2]
student_marks["Set"] = set(("test", "test1"))
student_marks["Dict"] = dict({"Hello": "World"})
print(student_marks)
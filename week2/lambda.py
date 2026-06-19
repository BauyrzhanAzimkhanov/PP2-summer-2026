import math
# lambda arguments : expression

# def x(a):
#     return a + 10

# x = lambda a : a + 10
# print(x(111))

# def multiplyTwoNumbers(a, b):
#     return a * b

# multiplyTwoNumbers = lambda a, b : a * b
# print(multiplyTwoNumbers(123456789, 9))

# def areaOfCircle(radius):
#     # return math.pi * radius * radius
#     return lambda radius : math.pi * radius**2

# resulting_function = areaOfCircle(1)

# print(resulting_function(100))

# def function(n):
#     print("n is", n)
#     return lambda a : a * n

# my_tripler = function(3)

# print(my_tripler(123))

# def double_item(item):
#     return item * 2

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(lambda item : item * 2, numbers))
# doubled_numbers = list(map(double_item, numbers))

# print(doubled_numbers)

# def willGetAMinusGrade(item):
#     return item >= 90 and item < 95

# studentMarks = [66, 78, 91, 83, 97, 100, 72, 85, 86]
# studentMarksForAMinusGrade = list(filter(lambda item : item >= 90 and item < 95, studentMarks))
# studentMarksForAMinusGrade = list(filter(willGetAMinusGrade, studentMarks))
# print(studentMarksForAMinusGrade)

# import json

# import os
# import math
# from re import RegexFlag


# print(abs(2))

# my_list = [False, False, False]
# print(all(my_list))

# print(any(my_list))

# my_tuple = ("red😀", "green", "blue")
# print(ascii(my_tuple))

# print(bin(15))

# print(bool(None))

# print(complex(-6.5, -2))

# print(dir())

# print(divmod(65, 9), 65 // 9, 65 % 9)

# my_operation = "a * b"
# my_global_vars = {"a": 5, "b": 87}
# print(eval(my_operation, my_global_vars))

# my_complex_operation = "for i in range(10):\n\tprint(i * i)"
# exec(my_complex_operation)

# print(format(43, 'X'))

# string_a = "Hello"
# string_b = "Hi"
# print(hash(string_a), hash(string_b))


# list_of_integers = [23, 4, -9, 56, 77]

# def get_reminder_on_div_by_3(number):
#     return int(number) % 3

# print(tuple(map(get_reminder_on_div_by_3, list_of_integers)))

# tuple_of_student_names = ("Almas", "Zhomart", "Bob", "Adolf")

# def filter_names_with_a_character(name):
#     if ("a" in name):
#         return False
#     else:
#         return True
    
# def filter_long_names(name):
#     return len(name) < 4

# print(tuple(filter(filter_long_names, tuple_of_student_names)))

# pc_vendors = ["HP", "Compaq", "Lenovo", "Dell", "Asus"]
# pc_vendors_dict = dict(enumerate(pc_vendors, 3))

# print(json.dumps(pc_vendors_dict))

# print(dict(enumerate(pc_vendors, 3)))

# boys = ["Azamat", "Ernur", "Adolf", "Van", "Ricardo"]
# girls = ["Aruna", "Dana", "Eva", "Nazym"]
# activities = ["Dance", "Draw", "Program", "Play football", "Sing"]

# pairs_with_activities = list(zip(boys, girls, activities))
# print(pairs_with_activities, "\n", * pairs_with_activities)
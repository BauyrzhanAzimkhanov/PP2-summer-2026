cars = ["Toyota", "Honda", "Suzuki"]
# cars = list(("Toyota", "Honda", "Suzuki"))
print(cars)

# i = 0
# while (i < len(cars)):
#     print("Car number", i + 1, ": ", cars[i])
#     i += 1

# i = 0
# for car in cars:
#     print("Car number", i + 1, ": ", car)
#     i += 1

cars.append("BMW")
print(cars)
cars.insert(1, "Ford")
print(cars)
# cars.clear()
# print(cars)
cars.pop(1)
print(cars)
cars.insert(1, "Ford")
print(cars)
cars.insert(1, "Ford")
print(cars)
cars.remove("Ford")
print(cars)
print(cars[2:4]) # cars [2, 4)
print(cars[-3:-2]) # cars [-3, -2)
cars.append("Chevrolet")
cars.append("Maseratti")
cars.append("Alfa Romeo")
print(cars)
print(cars[-3::2]) # [starting_index:index_of_the_finish_excluding_it:size_of_the_steps]
variables = [cars[0], 14, False, -8.32, cars[-5:-2:2]]
print(variables)
import pathlib
import os

# current_working_directory = pathlib.Path.cwd()
# home_directory = pathlib.Path.home()
# print(current_working_directory)

# new_position = current_working_directory / "week3"
# print(new_position)
# print(list(new_position.iterdir()))

# new_test_dir = pathlib.Path("week3/test")
# new_test_dir.mkdir()
# new_test_dir.rmdir()

# new_position = new_position.parents[1]
# print(new_position)
# print(list(new_position.iterdir()))

# new_position = pathlib.Path("/home/bauyrzhan/Downloads")
# new_postion = home_directory / "Downloads"
# print(new_position)
# print(list(new_position.iterdir()))


# file = open("README.md", "r")
# print(file.read())
# file.close()


with open("README.md", "r") as fi:
    print(fi.read())
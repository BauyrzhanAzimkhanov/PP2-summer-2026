import re

regular_expression = r"[a-z]+_[a-z]+@kbtu\.kz"

my_email = "ba_azimkhanov@kbtu.kz"

answer = re.match(regular_expression, my_email)

print(answer)
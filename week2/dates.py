import datetime

current_time = datetime.datetime.now()
print(current_time)

print(current_time.year)
print(current_time.strftime("%B - %d // %w"))

x = datetime.datetime(1889, 4, 20, 12, 34, 32, 346723)

print(x)
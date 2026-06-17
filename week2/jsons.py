import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(type(y))
print(y["age"])
for k,v in y.items():
    print(k, v)

my_dict = {
    "name": "Test",
    "value": 22,
    "price": 100.74
}

my_json = json.dumps(my_dict, indent=4, sort_keys=True)

print(my_json, type(my_json))
def printAreaOfRectangle(length, width):
    print("Area =", length * width)

def createOrderInCoffeeShop(volume, type="latte"):
    print("Order created.\nItem =", type, "\nVolume =", volume)

# printAreaOfRectangle(12, 4.5)
# createOrderInCoffeeShop(1)
# createOrderInCoffeeShop(2, "Cappuchino")

# *args, **kwargs
def printGuestNames(number_of_guests, party_default_parameter="default", *guest_names, **party_parameters):
    print("Number of guests:", number_of_guests)
    for i in guest_names:
        print(i)
    for k,v in party_parameters.items():
        print("Parameter:", k, "value:", v)

# printGuestNames(2, "Bob", "Jane", location="Almaty", time="22:00", host_of_the_party="William")

# lambda
def getVolumeOfObject(l, w, h):
    return l * w * h

my_lambda = lambda l, w, h: l * w * h
print(my_lambda(12, 2, 5))


global_variable = 1
print("global_varibale", global_variable)

def drawSquare():
    print("**\n**")
    local_variable = 2
    print("local_variable", local_variable)
    print("global_varibale", global_variable)
drawSquare()

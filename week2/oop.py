class Animal:
    def __init__(self, name):
        self.name = name
    
    def makeSound(self):
        print(self.name, "made sound.")
    
    weight = 10 

class Dog(Animal):
    def bark(self):
        print(self.name, "barked as dog.")
    # override
    def makeSound(self):
        print("We changed barking of", self.name)

class Wolf(Animal):
    def bark(self):
        print(self.name, "barked as wolf.")

# my_dog = Animal("Rex")
# my_dog.makeSound()
# print(my_dog.name)
# my_dog.weight *= 2
# print(my_dog.weight)

my_new_dog = Dog("Rex")
# my_new_dog.makeSound()
# my_new_dog.bark()

my_wolf = Wolf("Tom")
# my_wolf.bark()
my_list = [my_new_dog, my_wolf]
for i in my_list:
    # i.bark()
    i.makeSound()
    print(i.name, "has weight", i.weight)

class bankingAccount():
    def __init__(self, user_name):
        self.__assets = 0
        self.user_name = user_name
    
    def investFunds(self, funds):
        self.__assets += funds
    
    def viewAssets(self):
        print(self.__assets)

# my_bank_account = bankingAccount("James")
# my_bank_account.investFunds(2340)
# my_bank_account.viewAssets()

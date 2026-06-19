import random

class MyNumbers:
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.number <= 20:
            x = self.number # x - reference for number
            self.number += 1
            return x
        else:
            raise StopIteration

class randomBooleans():
    def __iter__(self):
        self.booleans = [True, False, None]
        return self
    def __next__(self):
        answer = random.choice(self.booleans)
        if (answer != None):
            return answer
        else:
            raise StopIteration

random_booleans = randomBooleans()
random_booleans_iterator = iter(random_booleans)

for i in random_booleans_iterator:
    print(i)

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)
class car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
car1 =car("blue", "sedan")
car2 = car("red", "suv")
print(car1.color,car2.model)
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"
for animal in [Dog(), Cat()]:
    print(animal.speak())
class SecretStash:
    def __init__(self):
        self.__chocolates = 10
    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

stash = SecretStash()
stash.take_chocolate()

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof! and {self.age} years old")
dog1 = dog("buddy", 3)
dog2 = dog("sare", 5)
dog1.bark()
dog2.bark()

        




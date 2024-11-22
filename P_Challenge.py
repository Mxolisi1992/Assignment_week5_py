class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

for animal in [Cat(), Dog()]:
    print(animal.speak())


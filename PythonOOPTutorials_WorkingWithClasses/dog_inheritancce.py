# Parent Class
class Dog:
    # Class Attribute
    species = "Mammal"

    # Initalizer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance Method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Instance Method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog Class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child Class (inherits from Dog Class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# Behaviours from parent classes

jim = Bulldog("Jim", 12)

print (jim)
print(jim.description())

# Child classes have specific attributes
# and behaviours as well

print(jim.run("Slowly"))


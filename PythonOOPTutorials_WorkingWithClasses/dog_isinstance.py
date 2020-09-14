#Parent class
class Dog:

    #Class attribute
    species = "mammal"

    #Initalizer / Instance Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance Method
    def description (self):
        return "{} is {} years old".format(self.name, self.age)

    #Instance Method
    def speak (self, sound):
        return "{} says {}".format(self.name, sound)

# Child class(inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child classes inherit attributes and
# Behaviors from the parent class

jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well

print(jim.run("Slowly"))


#Is Jim an instance of Dog ()
#Eventhough Jim is an instance of a subclass from Dog..
#..it is still an instance of Dog
print(isinstance(jim, Dog))

# Is Julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

#Is Johnny Walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

#Is Julie an instance of Jim
print(isinstance(julie, jim))
import random
class Pets:
    dogs = []

    #If you're holding ''instances'' need a list
    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print (dog.walk())
            # return ("%s is %s" % (dog.name, "walking"))


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def walk(self):
        return "%s is walking!" % (self.name)

    def eat(self):
        # return self.is_hungry == False
        self.is_hungry = False

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Assign 3 dog instances
list_of_dogs = [
    Bulldog("Tom", 6),
    Dog ("Fletcher", 7),
    RussellTerrier("Larry", 9)
]



# Assign the 3 dog instances to an instance of the pet class
# This is a variable assignment
my_pets = Pets(list_of_dogs)
(my_pets.walk())

# usually it's self.name.. but here it's my_pets.dogs like philo.name
print ("I have {} dogs".format(len(my_pets.dogs)))

for dog in my_pets.dogs:
    dog.eat()
    #For each element
    print ("{} is {}".format(dog.name, dog.age))

print ("And they're all {}, of course".format(Dog.species))

#state a variable as false
are_my_dogs_hungry = False

for dog in my_pets.dogs:
    if dog.is_hungry:
        #dog.is_hungry == True
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print(are_my_dogs_hungry)
    print("My dogs are hungry")

else:
    print(are_my_dogs_hungry)
    print("My dogs are not hungry")








# My solution
# class Pets:
#
#     species = "mammal"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description (self):
#         return "{} is {} years old".format(self.name, self.age)
#
#     def number_of_dogs(*args):
#         return len(args)
#
# Tom=Pets("Tom", 6)
# Fletcher=Pets("Fletcher", 7)
# Larry=Pets("Larry",96)
#
#
# print("I have {} dogs".format(Pets.number_of_dogs(Tom, Fletcher, Larry)))
# print(Tom.description())
# print(Fletcher.description())
# print(Larry.description())
# print("And they're all {} of course".format(Pets.species))

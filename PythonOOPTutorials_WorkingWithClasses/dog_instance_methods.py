#Real Python

class Dog:

    #Class Attribute
    species = "mammal"

    #Initalize / Instance Attributes
    def __init__(self,name, age):
        self.name = name
        self.age = age

    #instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    #Defining a 'behaviour' sound for that dog
    #It is not self.sound because it is not an attribute,
    #If want self.sound put it in the attribute and add it to the object's instance
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def mood(self, mood):
        return "{} is feeling {}".format(self.name, mood)


#Instantiate the Dog object
mikey = Dog("Mikey", 6)

print(mikey.description())
print(mikey.speak("Woof"))
print(mikey.mood("Happy"))




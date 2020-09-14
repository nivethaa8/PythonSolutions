#Real Python
class Dog:

    #Class Attribute
    species = "mammal"

    #Initalizer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age=age


    def get_biggest_number(self, *args):

        max_val=0
        for x in args:
            if x > max_val:
                max_val=x
                continue
            elif x < max_val:
                continue
        return max_val

# Instantiate the Dog object

philo = Dog("Philio", 5)
mikey = Dog("Mikey", 6)
ron = Dog("Ron", 10)
harry = Dog("Harry", 8)
hermoine = Dog("Hermoine", 1)

#Access the Instance Attributes
print ("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

#Is Philo a mammal
if philo.species == "mammal":
    print ("{0} is a {1}!".format(philo.name, philo.species))

print ("The Oldest Dog is {} years old".format(Dog.get_biggest_number(philo.age, mikey.age, ron.age, harry.age, hermoine.age)))


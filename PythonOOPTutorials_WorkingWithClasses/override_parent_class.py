class Dog:
    species = "mammal"

class someBreed (Dog):
    pass

class someOtherBreed(Dog):
    species = "Reptile"

frank = someBreed()
print (frank.species)

# breans = someOtherBreed()
# print(breans.species)

frank = someOtherBreed()
print (frank.species)


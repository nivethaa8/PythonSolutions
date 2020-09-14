from fib import fibonacci
import random
count =0

try:

    print ("Typical testing Inputs")
    print (fibonacci(10))
    print (fibonacci(40))
    print (fibonacci(50))

    print (" ")
    print ("Test Random Inputs")
    while count <10:
        n = random.randint(10,90)
        print (fibonacci(n))
        count = count +1

    print (" ")
    print ("Test Boundary Inputs")

    print (fibonacci(1))
    print (fibonacci(10000000))

except NameError:

    print ("Enter a number")
    quit()




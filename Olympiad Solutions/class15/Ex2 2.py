try:
    a=int (input ("Please enter a number: "))
    print ("%d + 5 = %d" % (a, a+5))

except NameError:
    print ("Invalid input, enter a number")

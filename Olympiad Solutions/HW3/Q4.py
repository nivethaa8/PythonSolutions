num_of_toonie = float (input ("How many toonies do you have? "))
num_of_loonie = float (input ("How many loonies do you have? "))
num_of_quarter = float (input ("How many quarters do you have? "))
num_of_dime = float (input ("How many dimes do you have? "))
num_of_nickel = float (input ("How many nickels do you have? "))

toonie = 2.00
loonie = 1.00
quarter = 0.25
dime = 0.10
nickel = 0.05

total = ((toonie * num_of_toonie) +
         (loonie * num_of_loonie) +
         (quarter * num_of_quarter) +
         (dime * num_of_dime) +
         (nickel * num_of_nickel))


print ("the total value of your coins comes out to $%.2f" % (total))


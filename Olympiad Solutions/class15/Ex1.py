n=float (input("Enter numerator"))
d=float (input ("Enter denominator"))

try:
    print ("The quotient is %.2f" % (n/d))

except ZeroDivisionError:
    print ("Divide by zero error. Please re-run with non-zero denominator")

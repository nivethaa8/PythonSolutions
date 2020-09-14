from fractions import gcd
num= input ("Enter the numerator: ")
den = input ("Enter the denominator: ")
x = gcd(num,den)
top = num/x
bottom = den/x

print ("The simplified fraction is: %d / %d " % (top, bottom))












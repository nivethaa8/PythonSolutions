def primenumber(n):
    """Determine if a number is prime"""
    for i in range (2,n):
        if (n%i) != 0:
            return True
        else:
            return False

print primenumber(11)


p = input ("Enter a number")
for x in range (2,p):
    check = True
# True until proved otherwise in for loop
# if false then will always remain false, so need to say true
    for i in range (2,x):
        if (x%i==0):
            check = False
    if check:
        print x

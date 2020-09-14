def primenumber(n):
    """Determine if a number is a prime number"""
    for i in range(2,n):
        while True:
            p = input ("Enter a number")
            if (n%i) != 0:
                for x in range (2,p):
                            check = True
# True until proved otherwise in for loop
# if false then will always remain false, so need to say true
                            for i in range (2,x):
                                if (x%i==0):
                                    check = False
                            if check:
                                print x

            else:
                return False

primenumber(11)






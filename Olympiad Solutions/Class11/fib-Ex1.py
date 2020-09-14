# Homework Class 11
# Nivethaa Nesarajah



def fib1(n):

    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


import time
n = 40
t1 = time.time()
a = fib1(n)
t2 = time.time()
print ("fib1(%d) = %d: %fs" % (n, a, t2-t1))

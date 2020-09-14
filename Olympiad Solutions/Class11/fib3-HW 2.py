import time

def fib3(n):
    if (n==1):
        return 1
    elif (n==2):
        return 2
    else:
        a=1
        b=1

        for i in range(1, n-1):
            c=a+b
            a=b
            b=c

        return c


n = 40
t1 = time.time()
x = fib3(n)
t2 = time.time()
print ("fib3(%d) = %d: %fs" % (n, x, t2-t1))





import time
import math

def fib2(n):

   for i in range(100001):
        phi=((1 + (math.sqrt(5)))/2)
        return int( ( ((phi)**n) - ((-1)**n)/ ((phi)**n) ) //(math.sqrt(5)))

n=40
t1=time.time()
a=fib2(n)
t2=time.time()
print ("fib2(%d) = %d: %fs" % (n, a, t2-t1))

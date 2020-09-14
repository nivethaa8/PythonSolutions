def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,(x%y))

print (gcd(48853, 1362899))

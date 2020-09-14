sum=0
num=0

for i in range (0,6):
    x=input("Enter a number")
    if (x%2!=0):
        sum=sum+x
    else:
        num=num+1

print ("The total sum of negative numbers is %d and number of positive numbers are %d" %(sum,num))

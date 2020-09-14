maxVal=int(input("Please enter a positive integer"))

num=0
sum=0
while True:
    num=num+1
    if num>maxVal:
        break
        # if negative does not count in code
    elif num % 2==0:
        continue
    else:
         sum=sum+num

print ("The sum of odd natural numbers small than or equal to" + str(maxVal) + "is" + str(sum))


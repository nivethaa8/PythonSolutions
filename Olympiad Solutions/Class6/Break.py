maxVal = int(input("Please enter a positive number"))

num=1
sumVal = 0
while True:
    if num > maxVal:
        break
    # If they enter a negative number
    sumVal=sumVal+num
    num=num+1



print ("The sum of the first " + str(maxVal) + " natural numbers is " + str(sumVal))


maxVal=int(input("Please enter a positive number"))
num=1
# Because it is positive Number
sumVal=0
while True:
    if num>maxVal:
        break
    sumVal=sumVal+num
    num=num+1

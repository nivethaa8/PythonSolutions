num1 = raw_input("Enter a number")
num2 = raw_input("Enter a number")
num3 = raw_input("Enter a number")
num4 = raw_input("Enter a number")
num5 = raw_input("Enter a number")

if (num1>=num2) and

minVal=int(min(num1, num2, num3, num4, num5))
maxVal=int(max(num1, num2, num3, num4, num5))

print ("The smallest number is: %d and the largest number is %d" % (minVal, maxVal))

minVal=0
count =0
maxVal=0

for i in range (0,5):
    num=raw_input ("Enter a number")

    while count<5:
        count=count+1
        for n in range(num):

        if  (minVal<0):
             minVal=0
             break

        elif (minVal<num):
             minVal=num
             continue

        elif (maxVal>num):
             maxVal=num
             continue
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

print (minVal, maxVal)


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3







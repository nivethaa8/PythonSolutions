num=input("Enter a number")
minVal=num
maxVal=num
count=0

while count<4:
        x=input("Enter a value")
        count=count+1

        if x>maxVal:
                maxVal=x
                continue
        elif x<minVal:
                minVal=x
                continue
        elif x<maxVal:
                continue
        else:
                continue




print (maxVal,minVal)


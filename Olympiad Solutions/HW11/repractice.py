import re

list = []
pattern = "\\w*oq" or "\\w*go" or "\\w*ow"  or "\\w*ugh "

with open ("/Users/nivethaanesarajah/Desktop/Python/Olympiads/Week 6/Class12_Python_Notes_and_Homework_Aug_08_Updated/InFlandersFields.txt", "r") as fileObj:
    for line in fileObj:

        x = re.findall(pattern, line, re.IGNORECASE)
        list.extend(x)

    num = len(list)

    print (num)



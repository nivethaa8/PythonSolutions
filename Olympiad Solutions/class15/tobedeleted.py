import re

list = []
list2= []
list3 = []
list4=[]

pattern = ("\\w*ow")
pattern2= ("\\w*go")
pattern3 = ("\\w*oe")
pattern4= ("\\w*ugh")

with open("/Users/nivethaanesarajah/Desktop/Python/Olympiads/Week 6/Class12_Python_Notes_and_Homework_Aug_08_Updated/InFlandersFields.txt", "r") as fileObj:
    for line in fileObj:

        s = re.findall(pattern, line, re.IGNORECASE)
        s2 = re.findall(pattern2, line, re.IGNORECASE)
        s3 = re.findall(pattern3, line, re.IGNORECASE)
        s4 = re.findall(pattern4, line, re.IGNORECASE)

        list.extend(s)
        list.extend(s2)
        list.extend(s3)
        list.extend(s4)


    num=len(list) + len(list2) + len(list3) + len(list4)
    print num


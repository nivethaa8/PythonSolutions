import re
list = [];
pattern = ("more")
with open ("/Users/nivethaanesarajah/Desktop/Python/Olympiads/Week 6/Class12_Python_Notes_and_Homework_Aug_08_Updated/TheRaven.txt", "r") as fileObj:
    for line in fileObj:
        match = re.findall(pattern, line)
        list.extend(match)

    print (list)
    print (len(list))



#print each line where string more appears
#print total

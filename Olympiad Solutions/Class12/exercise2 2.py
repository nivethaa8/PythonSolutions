import re
list = [];
list2 = [];

pattern = ("\\w*ore")
pattern2 = ("\\w*oor")
with open ("/Users/nivethaanesarajah/Desktop/Python/Olympiads/Week 6/Class12_Python_Notes_and_Homework_Aug_08_Updated/TheRaven.txt", "r") as fileObj:
    for line in fileObj:
        s = re.findall(pattern, line, re.IGNORECASE)
        s2 = re.findall(pattern2,line, re.IGNORECASE)
        list.extend(s)
        list2.extend(s2)

    num = (len(list)) + (len(list2))
    print num

# \w* specify zero or more characters
# print each line where a word rhymes with more



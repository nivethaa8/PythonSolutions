import random
list = []
count =0
#create a list of 10 numbers all less than 1000

while count <=10:
    list.append(random.randint(1,1000))
    count = count +1

print ("Old: " + str(list))
# x= sorted(list, key=None, reverse=False)
x = list.sort(key = None, reverse = False)
print ("New: " + str(list))

# print ("Unsorted list: " + str(list))
# print ("Sorted list: " +  str(x))





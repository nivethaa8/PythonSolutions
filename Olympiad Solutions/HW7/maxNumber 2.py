def maxNumber(x):
    """Takes a list argument, returns largest number"""
    maxVal = x[0]
    for num in x:
        if maxVal <num:
            maxVal=num
    return maxVal
print maxNumber([9,2,3,4])





#
# def highestNumber(l):
#     myMax = l[0]
#     for num in l:
#         if myMax < num:
#             myMax = num
#     return myMax
#
#
# print highestNumber ([77,48,19,17,93,90])

#
#         num=input ("Enter number")
#         list.append(num)
#         print (max(list))
#
#
#         # if list[i] > maxVal:
#         #     maxVal=i
#         # print(maxVal)
#
# def highestNumber(l):
#     myMax = l[0]
#     for num in l:
#         if myMax < num:
#             myMax = num
#     return myMax
#
#
# print highestNumber ([77,48,19,17,93,90])
#
#
#
# #
# # lst = []
# # num = int(input('How many numbers: '))
# # for n in range(num):
# #     numbers = int(input('Enter number '))
# #     lst.append(numbers)
# # print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
# # #
# #
# # def doubleStuff(aList):
# #     """ Overwrite each element in aList with double its value. """
# #     for position in range(len(aList)):
# #         aList[position] = 2 * aList[position]
# #
# # things = [2, 5, 9]
# # print(things)
# # doubleStuff(things)
# # print(things)

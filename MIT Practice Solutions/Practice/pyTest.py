import math
import statistics

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        # elt[] is a list, so append list in list
        new_stats.append([elt[0], elt[1], statistics.mean(elt[1])])
    return new_stats


# # avg function: version without an exception
# def avg(grades):
#     return (sum(grades))/len(grades)

# # avg function: version with an exception
# def avg(grades):
#     try:
#         return sum(grades)/len(grades)
#     except ZeroDivisionError:
#         print('warning: no grades data')
#         return 0.0


# # avg function: version with assert
# def avg(grades):
#     assert len(grades) != 0, 'warning: no grades data'
#     return sum(grades)/len(grades)


test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
               [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
               [['captain', 'america'], [80.0, 70.0, 96.0]],
               [['deadpool'], []]]

print(get_stats(test_grades))
# print(avg(avg(elt[1])))

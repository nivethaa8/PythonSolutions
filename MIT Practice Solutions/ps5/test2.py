x = 901000
values = []
negative = []

if (x > -(2 ** 31)) and (x < ((2 ** 31) - 1)):
    for e in str(x):
        values.append(e)

    if len(values) == 1:
        values_t = ''.join(values)
        print(values_t)

    # if len(values) > 1:
    #     if values[0] == "0":
    #         values.remove(values[0])

    if "-" in values:
        values.remove("-")
        negative.append("-")
    #
    # for i,e in enumerate (values):
    #     if values [0] == "0":
    #         # while "0" in values:
    #             values.remove("0")

    print(negative)

    values.reverse()
    if len(negative) > 0:
        values.insert(0, '-')

    values_t = ''.join(values)
    print(values_t)

else:
    exit()

# Homework 11
# Pascal Triangle
# Nivethaa Nesarajah


def pascal(n):
    print n
    if n==1:
        return [1]
    else:
        line = [1]
        print line
        previous_line = pascal(n-1)
    #Above executed before
    #Then the bottom is executed

        print ("what")
        print (previous_line)
        for i in range (len(previous_line)-1):
            print("test")
            line.append(previous_line[i] + previous_line[i+1])
        line +=[1]
    return line

print (pascal(4))

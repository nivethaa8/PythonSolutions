# Exercise 1:
# def nprint (message, n):
#     """This function prints a message n number of times"""
#     for x in range (n):
#         print (message)


def nprint (message, n=1):
    """This Function prints a  message n number of times"""
    for x in range(n):
        print (message)

# Exercise 3

def multiPrint (header, *messages):
    """This function prints any number of messages"""
    print (header)
    for x in messages:
        print ('\t' + x)

def listPrint (header, **list):
    """This function prints a list"""
    print (header)
    for key, value in list.items():
        print ('\t' + key + ':\t' + value)

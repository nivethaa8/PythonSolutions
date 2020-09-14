def palindrome(word):

    text = list(word)
    rev = text[::-1]

    for i in text:
        for x in rev:
            if (i==x):
                return True
            else:
                return False


print (palindrome("level"))


# for string, split character
# store character in a list = normal
# reverse the list = reversed
#compare normal = reversed
#else return false
#print word


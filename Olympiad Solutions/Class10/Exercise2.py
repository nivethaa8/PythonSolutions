import random
deck = dict()

for i in range(1,14):
    if i ==1:
        card = "A"
    elif i ==11:
        card = "J"
    elif i == 12:
        card = "Q"
    elif i ==13:
        card = "K"
    else:
        card = str(i)

    deck ["Spade " + card ] = i
    deck ["Heart " + card ] = i
    deck ["Club " + card ] = i
    deck ["Diamond " + card ] = i

print (deck)
print (len(deck))

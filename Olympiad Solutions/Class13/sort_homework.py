deck = dict()
import random
pile1 = dict()
pile2 = dict()
hand = dict()
count = 0



def shuffle (deck):
    test=10

    for i in range(1,14):
            if i == 1:
                card ="A"
            elif i == 11:
                card = "J"
            elif i ==12:
                card = "Q"
            elif i ==13:
                card = "K"
            else:
                card = str(i)

            deck["Spades" + card] = i

    for i in range(14,27):
            if i == 14:
                card ="A"
            elif i == 15:
                card = "J"
            elif i ==16:
                card = "Q"
            elif i ==17:
                card = "K"
            else:
                deck["Heart" + card] = i


    for i in range(27,40):
            if i == 27:
                card ="A"
            elif i == 28:
                card = "J"
            elif i ==29:
                card = "Q"
            elif i ==30:
                card = "K"
            else:
                card = str(i)

            deck["Club" + card] = i

    for i in range(40,53):
            if i == 40:
                card ="A"
            elif i == 41:
                card = "J"
            elif i ==42:
                card = "Q"
            elif i ==43:
                card = "K"
            else:
                card = str(i)

            deck["Diamond" + card] = i


    for i in range(1, 8):

        while len(deck) > 0:
            v=deck.popitem()

            if random.randint(0, 1) == 0:
                pile1[v[0]] = v[1]

            else:
                pile2[v[0]] = v[1]

        while len(pile1) > 0:
                v = pile1.popitem()
                deck[v[0]] = v[1]

        while len(pile2) > 0:
                v = pile2.popitem()
                deck[v[0]] = v[1]

# take a 13 card hand

shuffle(deck)
while count <13:
    count = count + 1
    v=deck.popitem()
    hand[v[0]]=v[1]

print hand
sort=sorted(hand,key=lambda k: hand[k])
print sort


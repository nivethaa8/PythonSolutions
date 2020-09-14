import random
deck1= dict()
deck2= dict()
deck3= dict()
deck4= dict()

for n in range (1,14):
        if n == 1:
            card = "A"
        elif n ==11:
            card = "J"
        elif n ==12:
            card = "Q"
        elif n == 13:
            card = "k"
        else:
            card = str(n)

        deck4 ["Diamond" + card] = n
        deck3 ["Club" + card] = n
        deck2 ["Heart" + card] = n
        deck1 ["Spade" + card] = n

#This is not in order
for x in deck1:
    hand[x] = deck1[x]
for y in deck2:
    hand[y] = deck2[y]
for z in deck3:
    hand[z] = deck3[z]
for p in deck4:
    hand[p] = deck4[p]


def shuffle (hand):
    pile1 = dict()
    pile2 = dict()
    for i in range(1,7):
        while len(hand) >0:
            v = hand.popitem()
            if random.randint(0,1) ==0:
                pile1[v[0]] = v[1]
            else:
                pile2[v[0]] = v[1]

        while len(pile1) >0:
            v=pile1.popitem()
            hand[v[0]] = v[1]

        while len(pile2) > 0:
            v = pile2.popitem()
            hand[v[0]] = v[1]

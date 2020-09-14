import random
deck = dict()
pile1 = dict()
pile2 = dict()
handlist = []
count = 0
hand=dict()
letter = []



for i in range(1, 14):

        if i == 1:
            card = "A"
        elif i == 11:
            card = "J"
        elif i == 12:
            card = "Q"
        elif i == 13:
            card = "K"
        else:
            card = str(i)

        deck["Spade " + card] = i
        deck["Heart " + card] = i
        deck["Club " + card] = i
        deck["Diamond " + card] = i

for i in range(1, 8):

        while len(deck) > 0:
                    # The 0,1 keeps going until all 52 cards are passed
            if random.randint(0, 1) == 0:
                v = deck.popitem();
                pile1[v[0]] = v[1]
                        # if it is 0 add the popped card, v to the top of the deck pile 1
            else:
                v = deck.popitem();
                        # if it is 1 add the popped card to the bottom of the deck pile 2
                pile2[v[0]] = v[1]

        while len(pile1) > 0:
                v = pile1.popitem();
                deck[v[0]] = v[1]

        while len(pile2) > 0:
                v = pile2.popitem();
                deck[v[0]] = v[1]

while count <13:
        count = count + 1
        v=deck.popitem()
        hand[v[0]]=v[1]

# hand_list = list(hand)
# print hand_list



# for i in range (len(hand_list)):
#     x = hand_list.pop()
#     letter.append(x[:1])

# print letter

#Sort by Spade, Heart, Club, Diamond
#Sort by number
#
# x= sorted (hand, key=lambda A: hand[A], K: hand[K], Q: hand[Q], J: hand[J], reverse=False)
#
#
correct_order = ['Spades', 'Heart', 'Club', 'Diamond']
x=sorted(hand, key = lambda n: correct_order.index(n[hand.keyitems]))
print x

#1-14 Spades
#15-28 Hearts
#29-

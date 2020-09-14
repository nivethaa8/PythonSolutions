import random
deck = dict()
pick1 = dict()
pick2 = dict()
pick3 =  dict()
pick4 = dict()
draw1 = dict()
draw2 = dict()
draw3 =  dict()
draw4 = dict()
draw5 = dict()
cheat = dict()

for i in range (1,14):
    if i == 1:
        card = "A"
    elif i == 11:
        card = "J"
    elif i == 12:
        card = "K"
    elif i ==13:
        card = "A"

    deck ["Spade" + card] = i
    deck ["Heart" + card] = i
    deck ["Club" + card] = i
    deck ["Diamond" + card] = i

def shuffle (deck):
   for i in range(1,8):

    pile1= dict()
    pile2= dict()

    while len(deck)>0:
        v= deck.popitem()
        if random.randint(0,1) == 0:
            pile1[v[0]] = v[1]
        else:
            pile2[v[0]] = v[1]

    while len(pile1)>0:
        v=pile1.popitem()
        deck[v[0]] = v[1]

    while len(pile2)>0:
        v=pile2.popitem()
        deck[v[0]] = v[1]

def deal():

    v = deck.popitem();
    pick1[v[0]] = v[1]

    v= deck.popitem();
    pick2[v[0]] = v[1]

    v=deck.popitem();
    pick3[v[0]] = v[1]

    v= deck.popitem();
    pick4[v[0]]=v[1]

    print pick1
    print pick2


def show():
    print pick3
    print pick4

def draw():

    v = deck.popitem()
    draw1[v[0]] = v[1]

    v= deck.popitem()
    draw2[v[0]] = v[1]

    v=deck.popitem()
    draw3[v[0]] = v[1]

    v= deck.popitem()
    draw4[v[0]]=v[1]

    v= deck.popitem()
    draw5[v[0]]=v[1]

    print draw1
    print draw2
    print draw3
    print draw4
    print draw5


def cheat ():

# convert a dictionary to a list
    cheatList = list(deck.items())
    print(cheatList[0])


#Start the game

gameChoice = str(raw_input ("What would you like to do \nPick: Deal, Draw, Show, Cheat, Quit: "))

while gameChoice.lower() != "quit":

        if gameChoice.lower() == "deal":
            shuffle(deck)
            deal()

        elif gameChoice.lower() == "draw":
            draw()

        elif gameChoice.lower() == "show":
            show()

        elif gameChoice.lower() == "cheat":
            deal()
            cheat()


        else:
            print ("try again")
        gameChoice = str(raw_input ("What would you like to do \nPick: Deal, Draw, Show, Cheat, Quit: "))




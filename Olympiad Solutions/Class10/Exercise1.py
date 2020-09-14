deck = set()

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

    deck.add ("Spade" + card)
    deck.add ("Heart"+ card)
    deck.add ("Club"+ card)
    deck.add ("Diamond"+ card)

    print (deck)
    print (len(deck))

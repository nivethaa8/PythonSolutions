class Card:

SPADE = "Spade"
HEART = "HEART"
CLUB = "Club"
DIAMOND = "Diamond"

Suits = (SPADE, HEART, CLUB, DIAMOND)
Ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank

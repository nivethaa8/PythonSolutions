class Card:
    SPADE = "Spade"
    HEART = "Heart"
    CLUB = "Club"
    DIAMOND = "Diamond"

    Suits = (SPADE, HEART, CLUB, DIAMOND)
    Ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.marked = False
    #can not access suits and rank outside the class, need to define functions with return
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getName(self):
        return self.suit + " " + self.rank

    def isMarked(self):
        return self.marked

    def setMarked(self, marked = True):
        self.marked = marked



#Final project
from random import randrange

Card_Val = ['Ace','1','2','3','4','5','6','7','8','9','10','J','Q','K']
Card_Sym = ['Spades','Hearts','Clubs','Diamonds']

class Deck:
    def __init__(self) -> None:
        self.cards = []
        for i in Card_Val:
            for j in Card_Sym:
                self.cards.append(i + ' ' + j)

    def getCard(self,deck):
        return




def split(card1, card2):
    if (card1 == card2):
        print("Do you like to SPLIT or NOT")
        res = input().upper()
        while True:
            if (res == "SPLIT"):
                print("Spliting")
                break
            elif (res == "NOT"):
                break
            else:
                print("Invalid response! Enter SPLIT or NOT.")
                res = input().upper()



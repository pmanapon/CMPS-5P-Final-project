#pseudo code
#Edited by Pattawut Manapongpun (Bill)


#getCard function - just use for checking my part
from random import randrange
class Deck:
    def __init__(self):
        Card_Val = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        Card_Sym = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.cards = []
        for i in Card_Val:
            for j in Card_Sym:
                self.cards.append(i + ' ' + j)

    def getCard(self,deck):
        randcard = deck[randrange(0,len(deck))]
        deck.remove(randcard)
        return randcard

    def getValue(self,card):
        if card[0] == 'A':
            return 1 #or 10
        elif card[0]=='J' or card[0]=='Q' or card[0]=='K':
            return 10
        elif card[0]=='1':
            return 10
        else:
            return int(card[0])


# newdeck = Deck()
# print(newdeck.cards)
# card1 = newdeck.getCard(newdeck.cards)
# print(card1)
# print(newdeck.getValue(card1))
#
# print(newdeck.cards)


def split(PlayCard1,PlayCard2):
    PlayCard1_1 = newdeck.getCard(newdeck.cards)
    PlayCard2_1 = newdeck.getCard(newdeck.cards)


#def hit():

#def double():

#def stand():


def startRound():

    newdeck = Deck()
    DealerCard1 = newdeck.getCard(newdeck.cards)
    PlayCard1 = newdeck.getCard(newdeck.cards)
    DealerCard2 = newdeck.getCard(newdeck.cards)
    PlayCard2 = newdeck.getCard(newdeck.cards)

    print("One of Dealer's card is " + DealerCard1)
    print("Your cards are " + PlayCard1 + " and " + PlayCard2)

    if PlayCard1[0] == PlayCard2[0]:
        print("Do you want to SPLIT hands? (Y/N)")
        if input().upper == 'Y':
            split(PlayCard1,PlayCard2)    #call split function

    print("Do you want to HIT or STAND or DOUBLE? (H/S/D)")
    res = input().upper()
    if res == 'H':
        hit()  #call hit function
    elif res == 'S':
        stand()     #call stand function
    elif res == 'D':
        double()    #call double function



# call bet function
startRound() #start round




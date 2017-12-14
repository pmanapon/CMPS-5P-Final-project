#pseudo code
#Edited by Pattawut Manapongpun (Bill)


#getCard function - just use for checking my part
from random import randrange
class Deck:
    def __init__(self):
        #♢♡♠♣♥♦
        Card_Val = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        Card_Sym = ['♠ Spades', '♥ Hearts', '♣ Clubs', '♦ Diamonds']
        self.cards = []
        #Create a deck of cards
        for i in Card_Val:
            for j in Card_Sym:
                self.cards.append(i + '' + j)

    def getCard(self,deck):
        '''Return a random card and delete it from deck'''
        randcard = deck[randrange(0,len(deck))]
        deck.remove(randcard)
        return randcard

    def getValue(self,card):
        '''Return the value of card'''
        if card[0] == 'A':
            return 1 #or 11
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

def getValue(card):
    '''Return the value of card'''
    if card[0] == 'A':
        return 1 #or 11
    elif card[0]=='J' or card[0]=='Q' or card[0]=='K':
        return 10
    elif card[0]=='1':
        return 10
    else:
        return int(card[0])

#Sammy part
def enter_money():
    money = float(input("please enter the total amount of money you wish to play with: "))
    if money<5:
        print("You do not have enough money to play with, please deposit more money!")
        exit()
    return money

def enter_bet():
    bet = int(input("please place a $5 minimum bet:"))
    while bet<5:
        print("Please enter at least the minimum bet to play.")
        bet=int(input())
    while bet>150:
        print("Your bet exceeds the maximum please enter a different amount")
        bet=int(input())
    print("Good luck!")
    return bet

def delay():
    import time
    print("loding....")
    time.sleep(1)

def split(PlayCard1,PlayCard2):
    print("Splitting...")
    global newdeck
    PlayCard1_1 = newdeck.getCard(newdeck.cards)
    PlayCard2_1 = newdeck.getCard(newdeck.cards)
    print("Hand1: " + PlayCard1 + " and " + PlayCard1_1 +" || Hand2: " + PlayCard2 + " and " + PlayCard2_1 )

#def hit():

#def double():

#def stand():


def startRound():

    global newdeck
    newdeck = Deck()
    DealerCard1 = newdeck.getCard(newdeck.cards)
    PlayCard1 = newdeck.getCard(newdeck.cards)
    DealerCard2 = newdeck.getCard(newdeck.cards)
    PlayCard2 = newdeck.getCard(newdeck.cards)

    # delay()
    print("One of Dealer's card is " + DealerCard1)
    # delay()
    print("Your cards are " + PlayCard1 + " and " + PlayCard2)



    if PlayCard1[0] == PlayCard2[0]:
        print("Do you want to SPLIT hands? (Y/N)")
        if input().upper() == 'Y':
            split(PlayCard1,PlayCard2)    #call split function



    print("Do you want to HIT or STAND or DOUBLE? (H/S/D)")
    res = input().upper()
    if res == 'H':
        PlayCard3 = newdeck.getCard(newdeck.cards) #call hit function
        print("Your cards are " + PlayCard1 + " and " + PlayCard2 + " and " + PlayCard3)
    elif res == 'S':
        stand()     #call stand function
    elif res == 'D':
        double()    #call double function

    while()




startRound()
# main
# money =  enter_money()
#
# while money > 0:
#     startRound() #start round
#
# print("You are out of money")
#
#
#

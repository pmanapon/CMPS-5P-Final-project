#Final Project
#Edited by Pattawut Manapongpun (Bill)

#####################################################################################################
# Main deck
#getCard function
from random import randrange
class Deck:
    def __init__(self):
        #♢♡♠♣♥♦
        Card_Val = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        Card_Sym = ['♠Spades', '♥Hearts', '♣Clubs', '♦Diamonds']
        self.cards = []
        #Create a deck of cards
        for i in Card_Val:
            for j in Card_Sym:
                self.cards.append(i + ' ' + j)

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
#######################################################################

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
        return 1 #return 1 for now but will add 10 later if needed
    elif card[0]=='J' or card[0]=='Q' or card[0]=='K':
        return 10
    elif card[0]=='1':
        return 10
    else:
        return int(card[0])

#Sammy part
def enter_money():
    money = int(input("Please enter the total amount of money you wish to play with: "))
    while money<5:
        print("You do not have enough money to play with, please deposit more money!")
        money = int(input("Please enter the total amount of money at least 5$: "))
    return money

def enter_bet():
    bet = int(input("Please place a $5 minimum bet: "))
    while bet<5:
        print("Please enter at least the minimum bet to play.")
        bet=int(input("bet: "))

    return bet

#############################################################################
def delay():
    import time
    print("loding....")
    time.sleep(1)


############################################################################
def split(PlayCard1,PlayCard2):
    print("Splitting...")
    global newdeck
    PlayCard1_1 = newdeck.getCard(newdeck.cards)
    PlayCard2_1 = newdeck.getCard(newdeck.cards)
    print("Hand1: " + PlayCard1 + " and " + PlayCard1_1 +" || Hand2: " + PlayCard2 + " and " + PlayCard2_1 )

def hit():
    global newdeck
    global PlayCard
    global PlaySum
    hitcard = newdeck.getCard(newdeck.cards)
    PlayCard.append(hitcard)  # call hit function
    print("Your cards are " + str(PlayCard))#PlayCard[0] , end="")
    # for i in range(1,len(PlayCard)):
    #     print(" || "+ PlayCard[i], end="")
    # print("")
    PlaySum += getValue(hitcard)


#def double():

#def stand():
####################################################################################
##########################################
def drawCards(cards):
    value=[]
    suit=[]
    for Acard in cards:
        if Acard[0] == '1':
            value.append("10")
        else:
            value.append(Acard[0]+".")

        if "♠" in Acard:
            suit.append("♠")
        elif "♣" in Acard:
            suit.append("♣")
        elif "♥" in Acard:
            suit.append("♥")
        elif "♦" in Acard:
            suit.append("♦")

    n = len(cards)
    for i in range(n):
        print(".------.\t", end="")
    print("")
    for i in range(n):
        print("|" + value[i] + "--. |\t", end="")
    print("")
    for i in range(n):
        print("|" + suit[i] + ":\/: |\t", end="")
    print("")
    for i in range(n):
        print("| :\/: |\t", end="")
    print("")
    for i in range(n):
        print("| '--'"+ suit[i] +"|\t", end="")
    print("")
    for i in range(n):
        print("`------'\t", end="")
    print("")
#########################################################
####################################################

def startRound():
    """Play one round and return win or lose"""
    global newdeck
    newdeck = Deck()
    global PlayCard
    PlayCard = [newdeck.getCard(newdeck.cards),newdeck.getCard(newdeck.cards)]
    DealerCard1 = newdeck.getCard(newdeck.cards)
    # PlayCard1 = newdeck.getCard(newdeck.cards)
    DealerCard2 = newdeck.getCard(newdeck.cards)
    # PlayCard2 = newdeck.getCard(newdeck.cards)
    DelerSum = 0
    global PlaySum
    PlaySum = getValue(PlayCard[0])+getValue(PlayCard[1])
    # delay()
    print("One of Dealer's card is " + DealerCard1)
    # delay()
    print("Your cards are " + str(PlayCard))#PlayCard[0] + " || " + PlayCard[1])



    if PlayCard[0][0] == PlayCard[1][0]:
        print("Do you want to SPLIT hands? (Y/N)")
        if input().upper() == 'Y':
            split(PlayCard1,PlayCard2)    #call split function


    print("Do you want to HIT or STAND or DOUBLE? (H/S/D)")
    res = input().upper()
    if res == 'H':
        PlayCard.append(newdeck.getCard(newdeck.cards)) #call hit function
        PlaySum += getValue(PlayCard[2])
        print("Your cards are " + str(PlayCard))#PlayCard[0] + " || " + PlayCard[1] + " || " + PlayCard[2])
    elif res == 'D':
        double()
    elif res == 'S':
        stand()     #call stand function
                   #call double function

    if PlaySum > 21:
        print("BUST!!!")
        return False

    while PlaySum<=21:
        print("Do you want to HIT or STAND (H/S)")
        res = input().upper()
        if res == 'H':
            hit()
        elif res == 'S':
            stand()

    if PlaySum > 21:
        print("BUST!!!")
        return False






#welcome()
money = enter_money()
bet = enter_bet()
money -= bet

print("Total money: {}  Bet: {}".format(money,bet))

while money >= 0:
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

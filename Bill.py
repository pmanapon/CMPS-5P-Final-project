#Final Project
#Edited by Pattawut Manapongpun (Bill)

#####################################################################################################
#Main deck
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
    for i in range(3):
        print("$")
        time.sleep(0.5)


##S##########################################################################
def split():
    print("Splitting...")
    global PlayCard
    global newdeck
    global PlaySum
    hand1 = [PlayCard[0], newdeck.getCard(newdeck.cards)]
    hand2 = [PlayCard[1], newdeck.getCard(newdeck.cards)]

    print("Hand1: " + str(hand1) + " and Hand2: " + str(hand2) )
    print("Hand1: ")
    drawCards(hand1)
    print("Total: " + str(point(hand1)))
    ####

    PlayCard = hand1.copy()
    PlaySum = getValue(hand1[0])+getValue(hand1[1])
    while PlaySum<=21:
        print("Hand1: Do you want to HIT or STAND (H/S)")
        res = input().upper()
        if res == 'H':
            hit()
        elif res == 'S':
            break
    bust=0
    if PlaySum > 21:
        print("Hand1 BUST!!!")
        bust=1

    hand1_c = PlayCard.copy()
    ###
    print("Hand2: ")
    drawCards(hand2)
    print("Total: " + str(point(hand2)))
    PlayCard = hand2
    PlaySum = getValue(hand2[0]) + getValue(hand2[1])
    while PlaySum<=21:
        print("Hand2: Do you want to HIT or STAND (H/S)")
        res = input().upper()
        if res == 'H':
            hit()
        elif res == 'S':
            return splitStand(hand1_c,PlayCard)
            break

    if PlaySum > 21 and bust==1:
        print("Hand2 BUST!!!")
        print("LL")
        return 'LL'
    elif PlaySum > 21:
        print("Hand2 BUST!!!")
        return splitStand(hand1_c, PlayCard)


def splitStand(hand1,hand2):
    global DealerCard
    global newdeck
    print("The dealer's cards are "+str(DealerCard))
    Hand1Point = point(hand1)
    Hand2Point = point(hand2)
    Dealpoint = point(DealerCard)

    # if Dealpoint > Hand1Point:
    #     print("Hand1: lose")
    #     Hand1Status = 'L'
    #
    # elif Dealpoint == Hand1Point:
    #     print("Hand1: Push")
    #     Hand1Status = 'P'
    #
    # if Dealpoint > Hand2Point:
    #     print("Hand2: lose")
    #     Hand2Status = 'L'
    #
    # elif Dealpoint == Hand2Point:
    #     print("Hand2: Push")
    #     Hand2Status = 'P'

    while Dealpoint < 17 and (Dealpoint < Hand1Point or Dealpoint < Hand2Point) :
        print("Dealer hit more card...")
        DealerCard.append(newdeck.getCard(newdeck.cards))
        Dealpoint = point(DealerCard)
        print("The dealer's cards are " + str(DealerCard))

    if Dealpoint > 21:
        print("Dealer's Busted")

    if Hand1Point > 21:
        Hand1Status = 'L'
    elif Dealpoint > 21:
        print("Hand1: Win")
        Hand1Status = 'W'
    elif Dealpoint < Hand1Point:
        print("Hand1: Win")
        Hand1Status = "W"
    elif Dealpoint > Hand1Point:
        print("Hand1: lose")
        Hand1Status ="L"
    elif Dealpoint == Hand1Point:
        print("Hand1: Push")
        Hand1Status ="P"



    if Hand2Point > 21:
        Hand2Status = 'L'
    elif Dealpoint > 21:
        Hand2Status = 'W'
    elif Dealpoint < Hand2Point:
        print("Hand2: Win")
        Hand2Status ="W"
    elif Dealpoint > Hand2Point:
        print("Hand2: lose")
        Hand2Status ="L"
    elif Dealpoint == Hand2Point:
        print("Hand2: Push")
        Hand2Status ="P"

    return Hand1Status+Hand2Status






#######################################################

def hit():
    global newdeck
    global PlayCard
    global PlaySum
    hitcard = newdeck.getCard(newdeck.cards)
    PlayCard.append(hitcard)  # call hit function
    print("Your cards are " + str(PlayCard))#PlayCard[0] , end="")
    drawCards(PlayCard)
    print("Total: " + str(point(PlayCard)))
    PlaySum += getValue(hitcard)

def double():
    global bet
    global money
    money -= bet
    bet *= 2
    print("Total money: {}  Bet: {}".format(money, bet))
    hit()



def stand(Playcard):
    Checkcard = PlayCard.copy()
    global DealerCard
    global newdeck
    print("The dealer's cards are "+str(DealerCard))
    Playpoint = point(Checkcard)
    Dealpoint = point(DealerCard)

    if Dealpoint > Playpoint:
        print("You lose")
        return "L"
    elif Dealpoint == Playpoint:
        print("Push")
        return "P"

    while Dealpoint < 17:
        print("Dealer hit more card...")
        DealerCard.append(newdeck.getCard(newdeck.cards))
        Dealpoint = point(DealerCard)
        print("The dealer's cards are " + str(DealerCard))


    if Dealpoint > 21:
        print("Dealer's busted")
        print("You win")
        return "W"
    elif Dealpoint < Playpoint:
        print("Win")
        return "W"
    elif Dealpoint > Playpoint:
        print("You lose")
        return "L"
    elif Dealpoint == Playpoint:
        print("Push")
        return "P"





#ASCII ART Functions
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

##Create a function to sum the value considering the value of Ace
def point(cards_in):
    cards = cards_in.copy()
    A = 0
    point = 0
    for Acard in cards:
        if Acard[0] == 'A':  #check no. of ace
            A += 1
        point += getValue(Acard)

    while (point<=11 and A>=1): #Ace can also be 11 so we add 10 if the sum is not over 21
        point += 10
        A -= 1

    return point





def startRound():
    """Play one round and return win or lose"""
    from time import sleep
    global newdeck
    newdeck = Deck()
    global PlayCard
    PlayCard = [newdeck.getCard(newdeck.cards),newdeck.getCard(newdeck.cards)]
    global DealerCard
    DealerCard = [newdeck.getCard(newdeck.cards),newdeck.getCard(newdeck.cards)]
    global PlaySum
    PlaySum = getValue(PlayCard[0])+getValue(PlayCard[1])
    global bet
    global money
    # sleep(1)
    print("One of Dealer's card is " + DealerCard[0])
    drawCards([DealerCard[0]])
    # sleep(1)
    print("Your cards are " + str(PlayCard))#PlayCard[0] + " || " + PlayCard[1])
    drawCards(PlayCard)
    print("Total: "+ str(point(PlayCard)))

    if point(PlayCard)==21:
        print("BlackJack!")
        return "BJ"

    print("Do you want to SPLIT hands? (Y/N)")
    if input().upper() == 'Y':
        return split()  # call split


    if PlayCard[0][0] == PlayCard[1][0]:
        print("Do you want to SPLIT hands? (Y/N)")
        if input().upper() == 'Y':
            split()    #call split function


    print("Do you want to HIT or STAND or DOUBLE? (H/S/D)")
    res = input().upper()
    if res == 'H':
        PlayCard.append(newdeck.getCard(newdeck.cards)) #call hit function
        PlaySum += getValue(PlayCard[2])
        print("Your cards are " + str(PlayCard))#PlayCard[0] + " || " + PlayCard[1] + " || " + PlayCard[2])
        drawCards(PlayCard)
        print("Total: " + str(point(PlayCard)))

    elif res == 'D':
        if money >= bet:
            double()
            return stand(PlayCard)
        else:
            print("You do not have enough money to double! ")

    elif res == 'S':
        return stand(PlayCard)     #call stand function
                   #call double function

    if PlaySum > 21:
        print("BUST!!!")
        return "L"

    while PlaySum<=21:
        print("Do you want to HIT or STAND (H/S)")
        res = input().upper()
        if res == 'H':
            hit()
        elif res == 'S':
            return stand(PlayCard)


    if PlaySum > 21:
        print("BUST!!!")
        return "L"






#welcome()
while True:
    print(startRound())



money = enter_money()
bet = enter_bet()
while True:
    print("Total money: {}  Bet: {}".format(money-bet,bet))
    res = input("Do you want to Deal! or Reset your bet?[D/R]: ").upper()
    if res == 'D':
        break
    else:
        bet = enter_bet()
money -= bet


# while money >= 0:

delay()
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

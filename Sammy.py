def welcome():

    print("""
 /$$      /$$           /$$                                                   /$$$$$$$$              /$$$$$$$  /$$                     /$$                               /$$       /$$
| $$  /$ | $$          | $$                                                  |__  $$__/             | $$__  $$| $$                    | $$                              | $$      | $$
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$          | $$  /$$$$$$       | $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$| $$
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$         | $$ /$$__  $$      | $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/| $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$         | $$| $$  \ $$      | $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/ |__/
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/         | $$| $$  | $$      | $$  \ $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$     
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$         | $$|  $$$$$$/      | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$|  $$$$$$$| $$ \  $$ /$$
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         |__/ \______/       |_______/ |__/ \_______/ \_______/|__/  \__/| $$ \_______/ \_______/|__/  \__/|__/
                                                                                                                                           /$$  | $$                          
                                                                                                                                           |  $$$$$$/                                                                                                                                                                          \______/                                  
    """)


def tutorial():
    print(input("Would you like a tutorial?:[y/n]"))
    if "y":
        print("""To begin playing you first enter the total amount of money that you
        
        would like to play with. Next you will be prompted to place at least the minimum bet. 
        
        Once you place at least the minimum bet, the dealer will distribute a maximum of two cards;
        
        first you, then the dealer and so on. Once you have two cards you will be asked to either hit, 
        
        stand, double down, or split depending on the cards you are dealt. For any total amount of cards 
        
        or combination you will be allowed to hit or stand; however, if you hit and the total value of your 
        
        cards exceeds 21 you will automatically lose. To split your cards, you must have two of the same 
        
        cards and only once the cards have been dealt. If you would like to double down it must be once the
         
         cards have been dealt and if you choose to you will receive 1 additional card. The caveat is that you 
         
         must match your inital bet to do this, however the plus side is that you will get 4 times the payout
          
         if you win. If you decide to stay, the dealer will be allowed to hit until his total cards have reached
           
         17 or greater. Once he exceeds 17 he will no longer be allowed to hit and at this point your total amount 
         
         of cards will be compared to his. If yours are greater you win and get an even payout, however if you lose
          
          the dealer takes your bet. On the chance that both you and the dealer have the same cards, you both push and 
          
          you neither lose or gain money. Now, have fun!
         
         """)

def bust():
    print("""
  ____  _    _  _____ _______ _ 
 |  _ \| |  | |/ ____|__   __| |
 | |_) | |  | | (___    | |  | |
 |  _ <| |  | |\___ \   | |  | |
 | |_) | |__| |____) |  | |  |_|
 |____/ \____/|_____/   |_|  (_)                                                      
    """)


def win():
    print("""
__  __               _       ___       __
\ \/ /___  __  __   | |     / (_)___  / /
 \  / __ \/ / / /   | | /| / / / __ \/ / 
 / / /_/ / /_/ /    | |/ |/ / / / / /_/  
/_/\____/\__,_/     |__/|__/_/_/ /_(_)   
                                         
    """)

def blackjack():
    print("""
       (                         )                         )   ____ ____ 
   (   )\ )    (        (     ( /(       (        (     ( /(  |   /|   / 
 ( )\ (()/(    )\       )\    )\()) (    )\       )\    )\()) |  / |  /  
 )((_) /(_))((((_)(   (((_) |((_)\  )\((((_)(   (((_) |((_)\  | /  | /   
((_)_ (_))   )\ _ )\  )\___ |_ ((_)((_))\ _ )\  )\___ |_ ((_) |/   |/    
 | _ )| |    (_)_\(_)((/ __|| |/ /_ | |(_)_\(_)((/ __|| |/ / (    (      
 | _ \| |__   / _ \   | (__   ' <| || | / _ \   | (__   ' <  )\   )\     
 |___/|____| /_/ \_\   \___| _|\_\\__/ /_/ \_\   \___| _|\_\((_) ((_)    
                                                                         
    """)





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
    drawCards(PlayCard)
    print("Total: " + str(point(PlayCard)))
    PlaySum += getValue(hitcard)

def double():
    global bet
    global money
    if money>=bet:
        money -= bet
        bet *= 2
        print("Total money: {}  Bet: {}".format(money, bet))
        hit()
        stand()
    else:
        print("You do not have enough money to double. ")

def stand():
    global PlayCard
    global DealerCard
    global newdeck
    print("The dealer's cards are "+str(DealerCard))
    Playpoint = point(PlayCard)
    Dealpoint = point(DealerCard)

    if Dealpoint > Playpoint:
        print("You lose")
        return "Lose"
    elif Dealpoint == Playpoint:
        print("Fair")
        return "Fair"

    while Dealpoint < 17:
        print("Deal hitted more card...")
        DealerCard.append(newdeck.getCard(newdeck.cards))
        Dealpoint = point(DealerCard)
        print("The dealer's cards are " + str(DealerCard))


    if Dealpoint > 21:
        print("Dealer's busted")
        print("You win")
        return "Win"
    elif Dealpoint < Playpoint:
        print("Win")
        return "Win"
    elif Dealpoint > Playpoint:
        print("You lose")
        return "Lose"
    elif Dealpoint == Playpoint:
        print("Fair")
        return "Fair"





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
    global newdeck
    newdeck = Deck()
    global PlayCard
    PlayCard = [newdeck.getCard(newdeck.cards),newdeck.getCard(newdeck.cards)]
    global DealerCard
    DealerCard = [newdeck.getCard(newdeck.cards),newdeck.getCard(newdeck.cards)]
    DelerSum = 0
    global PlaySum
    PlaySum = getValue(PlayCard[0])+getValue(PlayCard[1])
    # delay()
    print("One of Dealer's card is " + DealerCard[0])
    drawCards([DealerCard[0]])
    # delay()
    print("Your cards are " + str(PlayCard))#PlayCard[0] + " || " + PlayCard[1])
    drawCards(PlayCard)
    print("Total: "+ str(point(PlayCard)))


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
        drawCards(PlayCard)
        print("Total: " + str(point(PlayCard)))

    elif res == 'D':
        double()
    elif res == 'S':
        return stand()     #call stand function
                   #call double function

    if PlaySum > 21:
        print("BUST!!!")
        return "Lose"

    while PlaySum<=21:
        print("Do you want to HIT or STAND (H/S)")
        res = input().upper()
        if res == 'H':
            hit()
        elif res == 'S':
            return stand()


    if PlaySum > 21:
        print("BUST!!!")
        return "Lose"






welcome()
import time
time.sleep(1)

tutorial()



money = enter_money()
bet = enter_bet()
money -= bet

print("Total money: {}  Bet: {}".format(money,bet))

# while money >= 0:
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

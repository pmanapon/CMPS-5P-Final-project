import random

result = True

class blackjack:

    global result
    def __init__(self, money, bet):

        pokers = {"spade A": 1, "heart A": 1, "club A": 1, "diamond A": 1,
          "spade 2": 2, "heart 2": 2, "club 2": 2, "diamond 2": 2,
          "spade 3": 3, "heart 3": 3, "club 3": 3, "diamond 3": 3,
          "spade 4": 4, "heart 4": 4, "club 4": 4, "diamond 4": 4,
          "spade 5": 5, "heart 5": 5, "club 5": 5, "diamond 5": 5,
          "spade 6": 6, "heart 6": 6, "club 6": 6, "diamond 6": 6,
          "spade 7": 7, "heart 7": 7, "club 7": 7, "diamond 7": 7,
          "spade 8": 8, "heart 8": 8, "club 8": 8, "diamond 8": 8,
          "spade 9": 9, "heart 9": 9, "club 9": 9, "diamond 9": 9,
          "spade 10": 10, "heart 10": 10, "club 10": 10, "diamond 10": 10,
          "spade J": 10, "heart J": 10, "club J": 10, "diamond J": 10,
          "spade Q": 10, "heart Q": 10, "club Q": 10, "diamond Q": 10,
          "spade K": 10, "heart K": 10, "club K": 10, "diamond K": 10,}


        dealerCard = []
        dealer = {}
        playerCard = []
        player = {}

        global result
        result = True

        self.giveCards(pokers, dealer, player, dealerCard, playerCard)
        self.printDealer(dealerCard)  #show one card
        print('player', playerCard, '\n')
        while result == True:
            ans = input('What do you want to do? ..Hit: h..Stand:s..DoubleDown: d..Split: p..')
            if ans == 'h':
                self.hit(pokers, player, playerCard, dealer, dealerCard)
            elif ans == 's':
                self.stand(pokers, player, dealer, dealerCard, playerCard)
            elif ans == 'd':
                self.doubleDown(pokers, player, dealer, dealerCard, playerCard ,money, bet)
            #else: for the split

    def hit(self, pokers, player, playerCard, dealer, dealerCard):
        global result
        if self.checkNum(playerCard, player) < 21 and result == True:
            self.playerAddCard(pokers, dealer, player, playerCard)
            self.printDealer(dealerCard)
            print('player', playerCard, '\n')


    def stand(self, pokers, player, dealer, dealerCard, playerCard):
        global result
        if result == True:
            if self.checkNum(playerCard, player) < 21 and self.checkNum(dealerCard, dealer) < 17:
                while self.checkNum(dealerCard, dealer) < 17:
                    self.dealerAddCard(pokers, dealer, dealerCard)
                    if self.checkNum(dealerCard, dealer) == 21:
                        print('dealer', dealerCard, '\nplayer', playerCard, '\n')
                        self.exitGameLost() # don't have to exit, no case for the money
                    elif self.checkNum(dealerCard, dealer) > 21:
                        print('dealer', dealerCard, '\nplayer', playerCard, '\n')
                        self.exitGameWin()  # don't have to exit, no case for the money
            if self.checkNum(playerCard, player) < 21 and self.checkNum(dealerCard, dealer) < 21:
                if self.checkNum(playerCard, player) > self.checkNum(dealerCard, dealer):
                    print('dealer', dealerCard, '\nplayer', playerCard, '\n')
                    self.exitGameWin() # don't have to exit, no case for the money
                elif self.checkNum(playerCard, player) > self.checkNum(dealerCard, dealer):
                    print('dealer', dealerCard, '\nplayer', playerCard, '\n')
                    print('Push')  # don't have to exit, no case for the money
                else:
                    print('dealer', dealerCard, '\nplayer', playerCard, '\n')
                    self.exitGameLost() # don't have to exit, no case for the money
        result = False


    def giveCards(self, pokers, dealer, player, dealerCard, playerCard):
        for i in range(2):
            dCard, dNum = random.choice(list(pokers.items()))
            dealer[dCard] = dNum
            dealerCard.append(dCard)
            del pokers[dCard]

            pCard, pNum = random.choice(list(pokers.items()))
            player[pCard] = pNum
            playerCard.append(pCard)
            del pokers[pCard]


    def playerAddCard(self, pokers, dealer, player, playerCard):
        global result
        pCard, pNum = random.choice(list(pokers.items()))
        player[pCard] = pNum
        playerCard.append(pCard)
        del pokers[pCard]
        if self.checkNum(playerCard, player) == 21:
            print('dealer', dealer, '\nplayer', player, '\n')
            print('BLACKJACK!')
            self.exitGameWin()  # don't have to exit, no case for the money
            result = False
        elif self.checkNum(playerCard, player) > 21:
            print('dealer', dealer, '\nplayer', player, '\n')
            self.exitGameLost()  # don't have to exit, no case for the money
            result = False


    def dealerAddCard(self, pokers, dealer, dealerCard):
        dCard, dNum = random.choice(list(pokers.items()))
        dealer[dCard] = dNum
        dealerCard.append(dCard)
        del pokers[dCard]

#********************************************************************************************************
    def checkNum(self, c, p):  # need modify  (Ace = 1 or 11)
        sum = 0
        for i in range(len(c)):
            sum += p[c[i]]
        return sum
#********************************************************************************************************
   
   def printDealer(self, dealerCard):   #print dealer's card before stand
        temp = []
        for i in range(len(dealerCard)-1):
            temp.append(dealerCard[i+1])
        print('dealer',temp)


#************************** from pengze   *********************************
    def doubleDown(self, pokers, player, dealer, dealerCard, playerCard,money, bet):
        if len(playerCard) < 3 and money >= bet*2:
            self.hit(pokers, player, playerCard, dealer, dealerCard)
            bet *= 2
            return self.stand(pokers, player, dealer, dealerCard, playerCard)
        else:
            print("Sorry! You cannot choose Double Down!\n")


    def exitGameWin(self):
        print("The game is done! You WIN!")
        exit()


    def exitGameLost(self):
        print("The game is done! You LOST!")
        exit()
#***************************************


#************************** from Sammy  ******************
def enter_money():
    money=float(input("please enter the total amount of money you wish to play with:"))
    bet=int(input("please place a $5 minimum bet:"))
    if money<5:
        print("You do not have enough money to play with, please deposit more money!")
        exit()
    while bet<5:
        print("Please enter at least the minimum bet to play.")
        bet=int(input())
    while bet>150:
        print("Your bet exceeds the maximum please enter a different amount")
        bet=int(input())
    else:
        print("Good luck!")
        blackjack(money, bet)


enter_money()

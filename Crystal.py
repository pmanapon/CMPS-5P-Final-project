import random

def giveCards(pokers, dealer, player, dealerCard, playerCard):
    for i in range(2):
        dCard, dNum = random.choice(list(pokers.items()))
        dealer[dCard] = dNum
        dealerCard.append(dCard)
        del pokers[dCard]

        pCard, pNum = random.choice(list(pokers.items()))
        player[pCard] = pNum
        playerCard.append(pCard)
        del pokers[pCard]


def playerAddCard(pokers, player, playerCard):
    pCard, pNum = random.choice(list(pokers.items()))
    player[pCard] = pNum
    playerCard.append(pCard)
    del pokers[pCard]


def dealerAddCard(pokers, dealer, dealerCard):
    dCard, dNum = random.choice(list(pokers.items()))
    dealer[dCard] = dNum
    dealerCard.append(dCard)
    del pokers[dCard]


#*************************************************************************
def play():
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

    giveCards(pokers, dealer, player, dealerCard, playerCard)

#**********   for test
#    playerAddCard(pokers, player, playerCard)
#    for i in range(len(dealerCard)-1):
#        if dealer[dealerCard[i]] + dealer[dealerCard[i+1]] < 17:
#            dealerAddCard(pokers, dealer, dealerCard)
#**********

    print(dealer)
    print(player)

#******************************************************************************



play()

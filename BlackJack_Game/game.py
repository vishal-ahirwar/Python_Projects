from utils import askToContinue
from random import randint
CARDS=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def gameLoop():
    b_quit=False
    while(not b_quit):
        showGameInfo()
        user_card=pickupRandomCard()
        print(user_card)
        b_quit=askToContinue()
          
def showGameInfo():
    print("\n\nYou have 13 Cards [",end="")
    for card in CARDS:
        print(card,end=", ")
    print("]")

def pickupRandomCard():
    return CARDS[randint(0,len(CARDS)-1)]
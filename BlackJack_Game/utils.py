from art import LOGO,COPYRIGHT_NOTICE
from random import randint

def appInfo():
    print(LOGO)
    print(COPYRIGHT_NOTICE,end=" ")

def askToContinue():
    user_input=input("Would you like to play again?")
    if user_input.lower()=="yes" or user_input.lower()=="y":
        return False
    else:
        return True
    
def firstInit(user_card,computer_card,CARDS):
        user_card.append(pickupRandomCard(CARDS=CARDS))
        computer_card.append(pickupRandomCard(CARDS=CARDS))

def pickupRandomCard(CARDS):
    return CARDS[randint(0,len(CARDS)-1)]

def showGameInfo(CARDS):
    print("\n\nYou have 13 Cards [",end="")
    for card in CARDS:
        print(card,end=", ")
    print("]")


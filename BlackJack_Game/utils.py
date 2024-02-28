from art import LOGO,COPYRIGHT_NOTICE
from random import randint

def AppInfo():
    print(LOGO)
    print(COPYRIGHT_NOTICE,end=" ")

def AskToContinue():
    user_input=input("Would you like to play again?")
    if user_input.lower()=="yes" or user_input.lower()=="y":
        return False
    else:
        return True
    
def FirstInit(user_card,computer_card,CARDS):
        user_card.append(pickupRandomCard(CARDS=CARDS))
        computer_card.append(pickupRandomCard(CARDS=CARDS))

def PickupRandomCard(CARDS):
    return CARDS[randint(0,len(CARDS)-1)]

def ShowGameInfo(CARDS):
    print("\n\nYou have 13 Cards [",end="")
    for card in CARDS:
        print(card,end=", ")
    print("]")

def CalculateScore(cards):
     return sum(cards)
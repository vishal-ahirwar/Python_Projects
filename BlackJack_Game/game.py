from utils import askToContinue,showGameInfo,firstInit

CARDS=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=[]
computer_card=[]

def executeGameLoop():
    b_quit=False
    while(not b_quit):
        user_card.clear()
        computer_card.clear()

        showGameInfo(CARDS=CARDS)
        firstInit(user_card=user_card,computer_card=computer_card,CARDS=CARDS)

        b_quit=askToContinue()
          

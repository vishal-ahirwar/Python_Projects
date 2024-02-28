from utils import AskToContinue,ShowGameInfo,FirstInit,CalculateScore

CARDS=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=[]
computer_card=[]

def ExecuteGameLoop():
    b_quit=False
    while(not b_quit):
        user_card.clear()
        computer_card.clear()
        ShowGameInfo(CARDS=CARDS)
        FirstInit(user_card=user_card,computer_card=computer_card,CARDS=CARDS)
        b_quit=AskToContinue()
          

from art import LOGO,COPYRIGHT_NOTICE

def greet():
    print(LOGO)
    print(COPYRIGHT_NOTICE,end=" ")

def askToContinue():
    user_input=input("Would you like to play again?")
    if user_input.lower()=="yes" or user_input.lower()=="y":
        return False
    else:
        return True
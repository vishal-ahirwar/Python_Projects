import StartingLogo as sl
from random import randint

def GameOver():
  print(sl.EndingLogo);

  print('Quiting...')
  input('Enter Something to Quit Game...');
  return -1;

def CheckAnswer(Guess,Answer):
  if Guess >Answer:
    print("Too High");
    return False
  elif Guess <Answer :
    print("Too Low");
    return False
  elif Guess ==Answer:
    print(f"Correct Guess {Guess}");
    return True

def SetupDifficultyLevel():
  CanGo =False
  while CanGo ==False:
    DifficultyLevel =input('Please Difficulty level in "Easy", "Hard", "Medium" ??\n').lower();
    if DifficultyLevel =="easy":
      CanGo =True
      return 7;
    elif DifficultyLevel =="hard":
      CanGo =True
      return 15;
    elif DifficultyLevel =="medium":
      CanGo =True
      return int((7+15)/2)

def InitGame():
  sl.RunStartMessageFunction();
  answer =randint(1,100);
  MaxAttempts =SetupDifficultyLevel();
  print(f'You Have {MaxAttempts} Max Max Attempts to Guess The Correct Answer.');

  IsWon =False

  while MaxAttempts !=0 and IsWon ==False:
    Guess =int(input('Make Guess ...'));
    MaxAttempts-=1;
    print(f'You Have {MaxAttempts} left to Guess the Correct Answer ???');
    IsWon =CheckAnswer(Guess =Guess,Answer =answer);
  if IsWon ==False:
    print('You Failed to Guess The Correct Answer!');
  else:
    print(sl.WellDone);
    print('Well Done!');

  PlayAgain =input('Would You Like to Play Again ??\n[type : "yes" or "no"]\n').lower();
  if PlayAgain == "yes":
    InitGame();
  else:
    GameOver();

InitGame();



  











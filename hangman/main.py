
import random
import  HangmainWordList as hmwl
import Hangman_art as ha
print('Copyright©2021 "Hangman-MyVERSION" Vishal Ahirwar. All right reserved.\n')
print('Welcome to "Hangman" With Python!\n ')
print(ha.logo);

word_list = hmwl.word_list;
LifeLine = 0


PlayAgain = "Yes"

while PlayAgain.lower() == "yes" or PlayAgain.lower(
) == "yeah" or PlayAgain.lower() == "y":
    print(ha.logo);

    chosen_word = word_list[random.randint(0, len(word_list) - 1)]
    print(f'Random Choosen Word is : {chosen_word}.\n')
    LifeLine = len(chosen_word)

    disply = []
    for _ in chosen_word:
        disply.append('O_O')
    print(disply)
    while LifeLine > 0:
        guess = input('Guess a Letter : ').lower()
        LifeLine -= 1
        for pos in range(len(chosen_word)):
            if chosen_word[pos] == guess:
                disply[pos] = guess
        print(disply)
        print(f'You Have {LifeLine} Left\n')
    if "O_O" not in disply:
        print(f'Your Won!')
    else:
        print(f'You Lose!')
    PlayAgain = input('Would You Like to Play Again ???\n')

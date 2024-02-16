alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from logo import logo

run =True
while run:
  print(logo);
  print('Copyright© 2021 Vishal Ahirwar. All rights reserved.\n')
  ProceedForward =False
  while not ProceedForward:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower();
    if direction =="encode" or direction=="decode":
      ProceedForward =True
    else:
      print(f"Warning : Invalid Command!\n{direction}")
    
  ProceedForward =False

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift>26:
    shift%=26;

  def Cipher(text,shift,direction):
    Cipher_Text =""
    if direction =="decode":
      shift*=-1;
    for l in text:
      if l in alphabet:
        LCurrentPosition =alphabet.index(l);
        LNewPosition =LCurrentPosition+shift;
        Cipher_Text+=alphabet[LNewPosition];
      else:
        Cipher_Text+=l;
    print(f'Your {direction}ed Message : {Cipher_Text}\n');

  Cipher(text,shift,direction);

  E =input('Do You Wanted to run Again ??\n ').lower();
  if E =="no" or E == "not" or E == "nope":
    run =False
  else:
    run =True
print('\nGoodBye!...');

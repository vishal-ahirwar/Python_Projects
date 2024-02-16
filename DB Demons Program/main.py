from art import PrintArt
import data as dt
#print the art
PrintArt();

dt.GetAllUser(dt.data);
No_More =False
while No_More==False:
  dt.Login();
  Uwish =input("would you like to add more user ???\n[Type : yes or no ]\n").lower();
  if Uwish=="no":
    No_More =True
    print("All User on This Platform !\n\n");
    dt.GetAllUser(dt.data);

input("Quitting...");


#Fetch two random Accounts for Comparision

#compare them

#make loop of 


data =[
  {
    "name" : "Vishal",
    "age" : 17,
    "sex" : "male"
  },
  {
     "name" : "Simon",
    "age" : 27,
    "sex" : "male"
  },
  {
     "name" : "Piyush",
    "age" : 17,
    "sex" : "male"

  },
  {
     "name" : "Simi",
    "age" : 16,
    "sex" : "female"
  },
  
];

def AddUser():
  UserName =input("Please Enter Your Name ??");
  UserAge =int(input("please Enter Your Age ??"));
  UserSex =input("Please Enter Your Sex(Gender) : \n[male or female]\n");
  return {"name" : UserName,"age" : UserAge,"sex" : UserSex};

def Login():
  data.append(AddUser());

def GetAllUser(list):
  totalUser =0
  for _ in list:
    totalUser+=1;
  print(f"Total Number of Users : {totalUser}");
  print("--------------------------------------");
  print("--------------------------------------");
  Uwish =input("would You like to see All Users Info : ???\n[Type : yes or no]\n").lower();
  if Uwish =="yes":
    for l in list:
      for d in l:
        print(d, " : ",l[d]);
      print("\n-----------------\n"); 
  else:
    print("Okay ! as Your Wish...");
    




# print("your name has characters ",len(input("Enter your name ?")))
nested_list=[[1,2,3],['a','b','c'],["Vishal","Ahirwar"]]
for list in nested_list:
    for data in list:
        print(data,end="")
    print()
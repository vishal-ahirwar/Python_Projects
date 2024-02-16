
students={
    122209:"Vishal",
    122210:"Sam",
    122211:"Nik",
    122212:"mike"
    }

def printStudentsData(students):
    """This function takes dictionary and print out it's keys
    and values :)"""
    for roll_number in students:
        print(f"{roll_number}: {students[roll_number]}",end=",\n")


if __name__=="__main__":
    printStudentsData(students=students)
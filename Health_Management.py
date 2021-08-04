# Health management System Record with File
def getDate():
    import datetime
    return datetime.datetime.now()


def readPerson():
    with open("dataUser.txt", "rt") as f:
        print("Users List\n")
        count = 1
        lst = f.readlines()
        for i in range(0,len(lst)-1):
            print(str(count)+"  "+lst[i].strip())
            count += 1
        per = input("Which Data you want  to update")





def createData(name):

    try:
        with open('dataUser.txt', 'x') as f:
            f.write(name + '\n')
    except FileExistsError:
        with open("dataUser.txt", "r+") as cf:
            lst = cf.readlines()
            name = name + '\n'
            if name in lst:
                print('The User Already Exists')
                return -1
            else:
                cf.write(name + "\n")


def enterEntry():
    name = input("Enter the name of person\t")
    c = createData(name)
    if c != -1:
        opt = input("enter entry for diet or exercise\t").lower()
        if opt == "diet":
            with open("d_" + name + ".txt", "w") as f:
                date = str(getDate())
                f.write("\tDIET MANAGEMENT OF\t" + name + "\t\t\t JOIN AT (" + date + ") \n\n")
                print("USER INSERTION SUCESSED..................")
        elif opt == "exercise":
            with open("e_" + name + ".txt", "w") as f:
                date = str(getDate())
                f.write("\tEXERCISE MANAGEMENT OF\t" + name + "\t\t\t JOIN AT (" + date + ") \n\n")
                print("USER INSERTION SUCESSED..................")

        else:
            print("enter one of them or spell correctly")


def changeData(name):
    opt = input("What you want to modify (Diet / Exercise )\t").lower()
    if opt == "diet":
            with open("d_"+name+'.txt', 'r+') as f:
                date = str(getDate())
                food = input("what food had you eaten ?")
                f.write("\t"+food+"\t\t\t\t"+date+"\n" )
    elif opt == "exercise":
            with open("e_" + name + '.txt', 'r+') as f:
                date = str(getDate())
                exercise = input("what exercise you did ?")
                f.write("\t" + exercise + "\t\t\t\t" + date + "\n")

    else:
        print("please enter correct word !")




def modifyData():
    name=input("who you are? provide name")
    with open("dataUser.txt", "rt") as f:
        lst = f.readlines()
        lt = list()
        for i in range(0,len(lst)-1):
               lt.append(lst[i].strip())
        if name in lt:
            try:
                changeData(name)
            except FileNotFoundError:
                print("Your Entry does not created Till ")
        else:
            print("you are not the user")



def menu():
    print("1) enter new entry")
    print("2) modify history")
    ch = int(input("enter your choise\t"))
    if ch == 1:
        enterEntry()
    elif ch == 2:
        # readPerson()
        modifyData()


print("WELCOME TO THE WORLD OF HEALTH MANAGEMENT SYSTEM")
#  menu driven program
menu()

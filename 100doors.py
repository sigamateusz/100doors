import os
os.system('clear') # clear screen

def hundred_closed_doors():
    """Creating a hundred closed doors"""
    global doors
    for i in range(100):
        doors.append("close")


def toggle_the_door(n):
    """
    If the door is closed it opens
    If the door is opened it closes
    """
    global doors
    if doors[n]=="close":
        return "open"
    if doors[n]=="open":
        return "close"


def show_all_doors():
    """This function can show all doors"""
    for i in range(100):
        print("%3d." %(i+1), end=" ")
        print(doors[i])


def toggle_range(n):
    """Changes the status of all doors"""
    global doors
    for i in range(n-1,100,n):
        doors[i]=toggle_the_door(i)


def open_doors():
    """Prints all open doors """
    global doors
    print("The following doors are open: ")
    for i in range(100):
        if doors[i]=="open":
            print("%3d." %(i+1), end=" ")
            print(doors[i])

doors=[]

def main():
    hundred_closed_doors()
    for i in range(1,101):
        toggle_range(i)
    open_doors()


if __name__=="__main__":
    main()

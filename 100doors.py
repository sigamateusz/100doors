import os
os.system('clear') # clear screen

doors=[]

def main():
    for i in range(100):
        doors.append("close")
        print("%d" %(i+1), end=" ")
        print(doors[i])

if __name__=="__main__":
main()

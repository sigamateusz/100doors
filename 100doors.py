import os
os.system('clear') # clear screen

doors=[]
for i in range(100):
    doors.append("close")
    print("%d" %(i+1), end=" ")
    print(doors[i])

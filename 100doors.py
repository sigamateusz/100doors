import os
os.system('clear') # clear screen

doors=[False] * 100

for x in range(1,101):
    for i in range(x-1,100, x):
        doors[i] = not doors[i]

for i in range(100):
    if doors[i]==True:
        print("%3d.  Otwarte" %(i+1))

from random import *
zagad = str(randint(100,1000))
while zagad[0]==zagad[1] or zagad[0]==zagad[2] or zagad[1]==zagad[2]:

    zagad=str(randint(100,1000))
vvod=input()
while zagad!=vvod:

    bulls=0
    cows=0
    for i in range(len(zagad)):
        if zagad[i]==vvod[i]:
            bulls+=1
        if vvod[i] in zagad and zagad[i]!=vvod[i]:
            cows+=1
    if bulls==len(zagad):
        break
    print(f"коровы {cows}, быков {bulls}")
    vvod=input()
print("You win!")


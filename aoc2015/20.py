import math
final=150
final=33_100_000
houses={}
#we can reach minimu final with 10 times of final//10
times=10
times=11
for i in range(1,final//times+1,1):
    houses[i]=0
print("__")
try:
    for elf in range(1,final//times+1):
        for i in range(elf,final//times+1,elf):
            houses[i]+=elf*times
           
except:
    ...
#776160
for i in houses:
    if houses[i] >= final:
        print(i,houses[i])
        break
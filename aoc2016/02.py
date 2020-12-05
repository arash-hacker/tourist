f=open("02.txt")
pads=[
    [1,4,7],
    [2,5,8],
    [3,6,9]
]
pads2=[
    [0,0  ,1  ,0  ,  0],
    [0,2  ,3  ,4  ,  0],
    [5,6  ,7  ,8  ,  9],
    [0,'A','B','C',  0],
    [0,0  ,'D',0  ,  0],
]

pos=[1,1]
pos2=[0,2]
def move(line):
    global pos
    for c in line:
        if c=="L" and pos[0]>0:
            pos[0]-=1
        elif c=="R" and pos[0]<2:
            pos[0]+=1
        elif c=="D" and pos[1]<2:
            pos[1]+=1
        elif c=="U" and pos[1]>0:
            pos[1]-=1

def move2(line):
    global pos2
    for c in line:
        if c=="L" and pos2[0]>0 and pads2[pos2[1]][pos2[0]-1]!=0:
            pos2[0]-=1
        elif c=="R" and pos2[0]<4 and pads2[pos2[1]][pos2[0]+1]!=0:
            pos2[0]+=1
        elif c=="D" and pos2[1]<4 and pads2[pos2[1]+1][pos2[0]]!=0:
            pos2[1]+=1
        elif c=="U" and pos2[1]>0 and pads2[pos2[1]-1][pos2[0]]!=0:
            pos2[1]-=1
for line in f.readlines():
    #move(line)#82958
    move2(line)#5DB3
    print(pads2[pos2[1]][pos2[0]],end='')
    # print(pads[pos[0]][pos[1]],end='')


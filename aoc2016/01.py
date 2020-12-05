#!/bin/env python3
f=open("01.txt")
x,y,head=0,0,0
saved_xy=[(0,0)]
first_visited_x_y=[]

def chk(x,y):
    global first_visited_x_y,saved_xy
    if (x,y) not in saved_xy:
        saved_xy.append((x,y))
    elif not first_visited_x_y.__len__():
        first_visited_x_y=[x,y]
def rotate(RL):
    global x,y,head,saved_xy,first_visited_x_y
    if RL[0]=="R":
        head=(head+1)%4
    else:
        head=(head-1)%4
    pace=int(RL[1:])
    if head==0:#north
        for _ in range(0,pace):
            y+=1
            chk(x,y)
    elif head==1:#east
        for _ in range(0,pace):
            x+=1
            chk(x,y)
    elif head==2:#south
        for _ in range(0,pace):
            y-=1
            chk(x,y)
    else:#west
        for _ in range(0,pace):
            x-=1
            chk(x,y)

inputs=f.read().split(", ")
# f="R8, R4, R4, R8"
# inputs=f.split(", ")

for input in inputs:
    rotate(input)
        
print(
    x,
    y,
    head ,
    first_visited_x_y[0],
    first_visited_x_y[1])
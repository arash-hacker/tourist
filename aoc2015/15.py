l=[100,0,0,0]
"""
Sugar:       3,  0,   0,  -3,  2
Sprinkles:  -3,  3,   0,   0,  9
Candy:      -1,  0,   4,   0,  1
Chocolate:   0,  0,  -2,   2,  8
"""

calced_hash=set()
global_max=0
total_score=0
def deep(l,d=0):
    global global_max
    global total_score
    if str(l) in calced_hash or d>100 :
        return
    else:
        global_max=max(
            global_max,
            max(0, l[0]* 3  + l[1]*-3  +  l[2]*-1  + l[3]* 0)*
            max(0, l[0]* 0  + l[1]* 3  +  l[2]* 0  + l[3]* 0)*
            max(0, l[0]* 0  + l[1]* 0  +  l[2]* 4  + l[3]*-2)*
            max(0, l[0]*-3 +  l[1]* 0  +  l[2]* 0  + l[3]* 2)
        )
        if l[0]*2 +l[1]*9 +  l[2]*1  + l[3]*8 == 500:
            total_score=max(
                total_score,
                max(0, l[0]* 3  + l[1]*-3  +  l[2]*-1  + l[3]* 0)*
                max(0, l[0]* 0  + l[1]* 3  +  l[2]* 0  + l[3]* 0)*
                max(0, l[0]* 0  + l[1]* 0  +  l[2]* 4  + l[3]*-2)*
                max(0, l[0]*-3 +  l[1]* 0  +  l[2]* 0  + l[3]* 2)
            )
        calced_hash.add(str(l))
    deep([l[0]-1,  l[1]  ,    l[2]  ,   l[3]+1  ],  d+1)
    deep([l[0]-1,  l[1]  ,    l[2]+1,   l[3]    ],  d+1)
    deep([l[0]-1,  l[1]+1,    l[2]  ,   l[3]    ],  d+1)
    
deep(l)
print(str([10,20,30,40]) in list(calced_hash))

# print(sorted(list(calced_hash))[:50])
# print(sorted(list(calced_hash))[-50:])

print(global_max)
print(total_score)
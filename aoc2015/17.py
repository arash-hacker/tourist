import itertools
count=0
eggnog=25
containers=[20,15,10,5,5]
eggnog=150
containers=[11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3
]
ll=[]
for i in range(1,len(containers)+1):
    for j in list(itertools.combinations(containers,i)):
        if sum(j)==eggnog:
            ll.append(str(j))
            count+=1
print(set(ll).__len__())
print(count,len(ll),ll[0])
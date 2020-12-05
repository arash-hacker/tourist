f=open("03.txt")
lines=f.readlines()
import re
nums=re.compile(r"\s+(\d+)\s+(\d+)\s+(\d+)")
matches=0
for line in lines:
    m=nums.search(line)
    _1=int(m.groups(0)[0])
    _2=int(m.groups(0)[1])
    _3=int(m.groups(0)[2])
    if  _1+_2>_3 and \
        _2+_3 >_1 and \
        _1+_3 >_2:
        matches+=1
print(matches)
matches=0
import re
f=open("03.txt")
lines=f.readlines()
nums=re.compile(r"\s+(\d+)\s+(\d+)\s+(\d+)")
i=0
while i<len(lines):
    line1,line2,line3=lines[i:i+3]

    m1=nums.search(line1)
    m2=nums.search(line2)
    m3=nums.search(line3)

    _1_1=int(m1.groups(0)[0])
    _2_1=int(m1.groups(0)[1])
    _3_1=int(m1.groups(0)[2])
    _1_2=int(m2.groups(0)[0])
    _2_2=int(m2.groups(0)[1])
    _3_2=int(m2.groups(0)[2])
    _1_3=int(m3.groups(0)[0])
    _2_3=int(m3.groups(0)[1])
    _3_3=int(m3.groups(0)[2])

    if  _1_1 +_1_2 > _1_3 and \
        _1_2+_1_3 > _1_1 and \
        _1_3+_1_1 > _1_2 :
        matches+=1
    if  _2_1 +_2_2 > _2_3 and \
        _2_2+_2_3 > _2_1 and \
        _2_3+_2_1 > _2_2 :
        matches+=1
    if  _3_1 +_3_2 > _3_3 and \
        _3_2+_3_3 > _3_1 and \
        _3_3+_3_1 > _3_2 :
        matches+=1

    i+=3

print(matches)


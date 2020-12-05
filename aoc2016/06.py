from collections import Counter

f=open("06.txt")
lines=f.readlines()
codes=[]
for line in lines:
    codes.append(list(line))
tran_codes=list(zip(*codes))
for i in range(8):
    print(Counter(list(tran_codes[i])).most_common()[0][0],end="")
print()
for i in range(8):
    print(Counter(list(tran_codes[i])).most_common()[-1][0],end="")
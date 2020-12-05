import hashlib
i=0
x="ugkcyxxp"
answer={}
def _hash(i):
    return hashlib.md5(str(x+str(i)).encode()).hexdigest()
while len(answer)<=8:
    while not _hash(i).startswith("00000"):
        i+=1
    print(i,_hash(i))
    if '0'<=_hash(i)[5]<='8' and _hash(i)[5] not in answer:
        answer[_hash(i)[5]]=_hash(i)[6]
    i+=1
for i in range(8):
    print(answer[str(i)],end="")
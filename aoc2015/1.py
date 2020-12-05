f=open("1.txt","r")
st=f.readline()
i=0
counter=0
for c in st:
    if c==')':
        i-=1
    else:
        i+=1
    counter+=1
    if i==-1:
        print(counter)
        break
print(i)
st="1321131112"
#6989950
for j in range(40): 
    out=""
    which=st[0]
    much=1
    for c in st[1:]:
        if which==c:
            much+=1
        else:
            # out=out+str(much)+str(which)
            out=out+str(much)+str(which)
            which=c
            much=1
    out=out+str(much)+str(which)
    st=out
    print(j,st)
print(len(out))
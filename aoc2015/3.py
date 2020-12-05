f=open("3.txt","r")
st=f.read()
xx,yy,x,y,i = 0,0,0,0,1
#<v^^>
se=set({(0,0)})
for c in st:
    if i%2==0:
        if c=='^':
            x+=1
        elif c=='<':
            y-=1
        elif c=='>':
            y+=1
        elif c=='v':
            x-=1
        se.add((x,y))

    else:
        if c=='^':
            xx+=1
        elif c=='<':
            yy-=1
        elif c=='>':
            yy+=1
        elif c=='v':
            xx-=1
        se.add((xx,yy))
            
    i+=1
    
print(len(se),i)
    
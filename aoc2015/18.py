f=open("18.txt")
grids=f.read().splitlines()

def neighbor(i,j):
    res=[]
    global grids
    ( 0 <= i   <= len(grids[0])-1 ) and  ( 0 <= j-1 <= len(grids)-1 ) and grids[i][j-1]  =="#" and res.append(True)
    ( 0 <= i   <= len(grids[0])-1 ) and  ( 0 <= j+1 <= len(grids)-1 ) and grids[i][j+1]  =="#" and res.append(True)
    ( 0 <= i-1 <= len(grids[0])-1 ) and  ( 0 <= j   <= len(grids)-1 ) and grids[i-1][j]  =="#" and res.append(True)
    ( 0 <= i+1 <= len(grids[0])-1 ) and  ( 0 <= j   <= len(grids)-1 ) and grids[i+1][j]  =="#" and res.append(True)
    ( 0 <= i-1 <= len(grids[0])-1 ) and  ( 0 <= j-1 <= len(grids)-1 ) and grids[i-1][j-1]=="#" and res.append(True)
    ( 0 <= i+1 <= len(grids[0])-1 ) and  ( 0 <= j+1 <= len(grids)-1 ) and grids[i+1][j+1]=="#" and res.append(True)
    ( 0 <= i-1 <= len(grids[0])-1 ) and  ( 0 <= j+1 <= len(grids)-1 ) and grids[i-1][j+1]=="#" and res.append(True)
    ( 0 <= i+1 <= len(grids[0])-1 ) and  ( 0 <= j-1 <= len(grids)-1 ) and grids[i+1][j-1]=="#" and res.append(True)
    return res    

def gen():
    next_gen=[]
    for i in range(len(grids[0])):
        next_gen.append(list(grids[i]))
        for j in range(len(grids)):
            res=grids[i][j]

            if (i==0 or i==99 ) and (j==0 or j==99):
                res="#"
            elif res=='#':# on
                if sum(neighbor(i,j))!=2 and sum(neighbor(i,j))!=3:
                    res="."
            else:# off
                if sum(neighbor(i,j))==3:
                    res="#"
            next_gen[i][j]=res
        next_gen[i]=''.join(next_gen[i])
    return next_gen

for i in range(100):
    grids=gen()

print(sum([True for i in grids for j in i if j =="#"]) )
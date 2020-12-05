f=open('14.txt')
f=f.read()
l={}
def run(time,speed,second,rest):
    if time % (rest+second)<= second-1 :
        return speed
    else:
        return 0
for st in f.splitlines():
    x,_,_,speed,_,_,second,_,_,_,_,_,_,rest,_=st.split(' ')
    l[x]={}
    l[x]["speed"]=int(speed)
    l[x]["second"]=int(second)
    l[x]["rest"]=int(rest)
    l[x]["count"]=0
    l[x]["score"]=0
for i in range(2503):
    for x in l:
        l[x]["count"]+=run(i,
            l[x]["speed"],
            l[x]["second"],
            l[x]["rest"])
    maxx = max(map(lambda x:l[x]["count"],l))   
    y=[x for x in l if l[x]['count']== maxx]
    for yy in y:
        l[yy]["score"]+=1
    print("--------"+str(i+1)+"---------")
    print(list(map(lambda x:l[x]["count"],l)))
    print(list(map(lambda x:l[x]["score"],l)))
    print("-------------------")
print(list(map(lambda x:(x,l[x]["score"]),l)))
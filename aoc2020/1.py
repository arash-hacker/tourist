f=open('1.txt')
st=f.readlines()
def calc():
    for i in st:
        for j in st:
            if i!=j and int(i)+int(j)==2020:
                print( int(i)*int(j) )
                return
#calc()
def calc2():
    for i in st:
        for j in st:
            for k in st:
                if i!=j!=k and int(i)+int(j)+int(k)==2020:
                    print(int(i)*int(j)*int(k))
                    return
calc2()


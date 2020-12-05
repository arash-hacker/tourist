import re 
f=open("2.txt")
st=f.readlines()
i=0
def is_correct(ins):
    
    inss=ins.split(' ')
    [mn,mx]=inss[0].split('-')
    w=inss[1][0]
    string=inss[2]
    mn,mx=int(mn),int(mx)
    if w in string and ((string[mn-1]==w) +  (string[mx-1]==w)==1):
        return True
    else:
        print(w,inss,string)
        return False

for ins in st:
    if is_correct(ins):
        i+=1
print(i)
print(

is_correct("1-3 a: abcde"),
is_correct("1-3 b: cdefg"),
is_correct("2-9 c: ccccccccc"),

)

import re 
import string
import re
xXX=re.compile(r"\\\\x[0-9a-f][0-9a-f]")
double_backslashes=re.compile(r"\\\\")
slash_sth=re.compile(r"\\.")

f=open("8.txt","r")
f=f.read()
i,j,k=0,0,0
# for st  in f.splitlines():
#     x=re.sub(r"\\\\","-",st)
#     x=re.sub(r"\\\"","*",x)
#     x=re.sub(r'\\x[0-9a-fA-F][0-9a-fA-F]','*',x)
#     x=x.replace("\\\\","*").replace(r'','_').split('_')

#     i+=len(st)
#     j+=(len(x)-4)
# print(i,j,k,i-j)
for st  in f.splitlines():
    x=re.sub(r"\\\\","----",st)
    x=re.sub(r"\\\"","****",x)
    x=re.sub(r'\\x[0-9a-fA-F][0-9a-fA-F]','*****',x)
    x=x.replace("\\\\","****").replace(r'','_').split('_')

    i+=len(st)
    j+=(len(x))+2
    print(st,len(st),len(x))
print(i,j,j-i)
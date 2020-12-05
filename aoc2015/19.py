
# part 1
# f=open("19.txt")
# lines=f.read().splitlines()
# hashes={}
# distinc_strings=set([])
# string=""
# for i in lines:
#     x,*y=i.split(" => ")
#     if y == []:
#         string=x
#     else :
#         if x not in hashes:
#             hashes[x]=[]
#         hashes[x].append(y[0])
# for key in hashes:
#     rere=re.compile(key)
#     indexes=list(rere.finditer(string))
#     for index in indexes:
#         for option in hashes[key]:
#             new_string=list(string)
#             new_string[index.start():index.end()]=option
#             distinc_strings.add(''.join(new_string))
# print(len(distinc_strings))
import re
f=open("19.txt")
lines=f.read().splitlines()
hashes={}
generated_strings=[]
generated_strings2=[]
string=""
for i in lines:
    x,*y=i.split(" => ")
    if y == []:
        string=x
    else :
        y=y[0]
        if y not in hashes:
            hashes[y]=[]
        hashes[y].append(x)


generated_strings.append(string)
goal="e"  
success=[]
i=0
while len(generated_strings)>0:
    sorted(generated_strings,key=len)
    string=generated_strings.pop()
    print(i,len(generated_strings),len(string))
    i+=1
    # if i > 10_000:
    #     break
    for key in hashes:
        rere=re.compile(key)
        indexes=list(rere.finditer(string))
        for option in hashes[key]:
            for index in indexes:
                new_string=list(string)
                new_string[index.start():index.end()]=option
                new_string=''.join(new_string)
            if new_string==goal:
                success.append(new_string)
                raise Exception()
            if len(new_string)>0 and   new_string not in generated_strings2:
                generated_strings.append(new_string)
                generated_strings2.append(new_string)
print(len(success))







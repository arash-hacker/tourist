f=open("04.txt")
lines=f.read().splitlines()
import re 
from collections import Counter

sector_ids=0
id_matcher=re.compile("([a-z0-9-]+)\[(.+)\]")
for line in lines:
    m=id_matcher.search(line)
    id,code=Counter(''.join(m.groups(0)[0].split('-')[:-1]).replace('-','')),m.groups(0)[1]
    id={k:v for k,v in sorted(id.items(),key=lambda item:item[1],reverse=True)}
    match_regex={}
    match_regex_string=[]
    for k,v in id.items():
        if v in match_regex:
            match_regex[v].append(k)
        else:
            match_regex[v]=[k]

    # print(match_regex)

    eq_than_5=0
    for k in match_regex:
        eq_than_5+=len(match_regex[k])
        if eq_than_5<0:#when passed over 5 many times ago
             pass
        elif eq_than_5>=5 and k!=1:#trigger when we passed once step after 5
            x=str(5-(eq_than_5-len(match_regex[k])))# we calc how much need to exact five length
            eq_than_5=-10000000
            match_regex_string+="("+'|'.join(match_regex[k])+")"+"{"+x+"}"
        elif k==1 : # when reached to 1 and only 1
                match_regex_string+="("+'|'.join(match_regex[k])+")"+"{0,}"
        else:#before get to five 
            match_regex_string+="("+'|'.join(match_regex[k])+")"+"{"+str(len(match_regex[k]))+"}"

    match_regex_string=''.join(match_regex_string) 
    check_with_code=re.compile(match_regex_string)
    if check_with_code.match(code) is not None:
        sector_ids+=int(m.groups(0)[0].split('-')[-1])
        print(match_regex_string)
        print('YES',m.groups(0)[0],code)
    else:
        print(match_regex_string)
        print('NO',m.groups(0)[0],code)

print(sector_ids)
# import re

# def up(string,times):
#     out=[]
#     for c in string:
#         if c=='-':
#             out.append(' ')
#         else:
#             out.append( chr(  ((ord(c)-97)+(times%26))%26+97  ) )
#     return ''.join(out)
# f=open("04.txt")
# lines=f.readlines()
# id_matcher=re.compile("([a-z0-9-]+)\[(.+)\]")
# for line in lines:
#     m=id_matcher.search(line)
#     times=int(m.group(1).split('-')[-1])
#     out=up('-'.join(   list(m.group(1).split('-')[:-1])   ),times)
#     if "northpole" in out:
#         print(times,m.group(1))
#         break
#     print(out)
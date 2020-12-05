import re
bracket=re.compile(r"\[(\w+)\]")
reverse=re.compile(r"(\w)(\w)\2\1")
aba=re.compile(r".*(\w)(\w)\1.*\[.*\2\1\2.*\].*")
bab=re.compile(r".*\[.*(\w)(\w)\1.*\].*\2\1\2.*")
wrong_aba=re.compile(r".*\[.*(\w)(\w)\1.*\].*\[\w*\1\2\1\w*].*")
trick=re.compile(r"(\w)(\w)\1.*\2\1\2")


f=open("07_2.txt")
lines=f.read().splitlines()


def isABBA(string):
    m=reverse.search(string)
    if m is not None and m.group(1)!=m.group(2):
        return True
    else:
        return False
def isABA(s):
    t=trick.search(s)
    if t and t.group(1)!=t.group(2) and (('[' in t.group()) ^ (']' in t.group())):
        #print('YES',t.group())
        return True
    else:
        print('FALSE',t.group())
        return False
    # m=aba.search(s)
    # n=bab.search(s)
    # if  (m is not None and m.group(1)!=m.group(2))^(n is not None and n.group(1)!=n.group(2)):
    #     print(s)
    #     return True
    # else:
    #     return False
def parse(string):
    m=bracket.search(string)
    if m is not None:# still bracket exists
        if isABBA(m.group(1)):
            return False
        else:
            string=list(string)
            string[m.start():m.end()]=['_']
            string=''.join(string)
            return parse(string)
    else:# outsite []
        return isABBA(string)

print(sum([isABA(line) for line in lines]))
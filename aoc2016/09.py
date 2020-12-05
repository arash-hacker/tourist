f=open("09.txt")
line=f.read().splitlines()[0]
lines=[
    "ADVENT",#5
    "A(1x5)BC",#7
    "(3x3)XYZ",#9
    "A(2x2)BCD(2x2)EFG",#11
    "(6x1)(1x3)A",#6
    "X(8x2)(3x3)ABCY",#18
]
line=[
    "(27x12)(20x12)(13x14)(7x10)(1x12)A",#241920
    # "(3x3)XYZ",#9
    # "X(8x2)(3x3)ABCY",#20
    # "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN",#445
]
import re
r=re.compile(r"\((\d+)x(\d+)\)")
def calc(string):
    sum=0
    while len(list(r.finditer(string)))>0:
        m=r.search(string)
        string=list(string)
        string[m.start():m.end()+int(m.group(1))]=[]
        string=''.join(string)
        sum+=int(m.group(1))*int(m.group(2))
    sum+=len(string)
    return sum
def calc2(string):
    if len(list(r.finditer(string)))>0: m=r.search(string) return len() else: return len(string) while len(list(r.finditer(string)))>0: m=r.search(stri
        string[m.start():m.end()+int(m.group(1))]=string[m.end():m.end()+int(m.group(1))]*int(m.group(2))
        string=''.join(string)
    return len(string)

print(calc2(line[0]))
# for line in lines:
#     print(calc2(line))

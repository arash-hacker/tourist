import re
first="vzbxkghb"
successive_chars=re.compile(r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|012|123|234|345|456|567|678|789)")
overlap_pair=re.compile(r"([a-z])\1.*([a-z])\2")
oil=re.compile(r"[oil]")
def is_three_increase(st):
    return successive_chars.search(st) is not None
def is_non_overlap_pair(st):
    return overlap_pair.search(st) is not None
def is_not_oil(st):
    return oil.search(st) is None

def is_valid(st):
    return is_three_increase(st) and is_non_overlap_pair(st) and is_not_oil(st)
def inc(st,i=-1):
    st=list(st)
    if st[i]!='z':
        st[i]= chr(ord(st[i])+1)
        return ''.join(st)
    else:
        st[i]='a'
        return inc(''.join(st),i-1)
for i in range(1,1_000_000_000):
    first=inc(first)
    if is_valid(first):
        print(first)
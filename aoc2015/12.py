# import re
# f=open('12.json')
# f=f.read()
# no_red=re.sub(r'{.*\:\"red\".*}',"{}",f)
# print(no_red,"-----")
# num_=re.compile('[-0-9]*')
# l=num_.findall(no_red)
# import pdb; pdb.set_trace()

# print(l)
# print(sum([int(i) for i in l if i != '']))
import json
import sys

def dosum(obj):
    localsum = 0
    keep = list()
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str):
                if v == "red":
                    return 0
            if isinstance(v, int):
                localsum += v
            if isinstance(v, (list, dict)):
                keep.append(v)
    else:
        for v in obj:
            if isinstance(v, int):
                localsum += v
            if isinstance(v, (list, dict)):
                keep.append(v)
    for x in keep:
        localsum += dosum(x)
    return localsum

with open('12.json') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
data = json.loads(lines[0])
print(dosum(data))
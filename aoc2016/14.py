#!/bin/env python
import hashlib
import re
ddd=re.compile(r"(.)\1\1")
ddddd=re.compile(r"(.)\1\1\1\1")

key="jlmsuwbz"
#key="abc"
k=0
def streched_hash(string):
    for i in range(2016):
        string=hashlib.md5((string).encode()).hexdigest()
    return string
"""
for i in range(1_000_000):
   gen=streched_hash(hashlib.md5((key+str(i)).encode()).hexdigest()) 
   if m:=ddd.search(gen):
       has_bad=True
       for j in range(i+1,i+1000):
           gen2=streched_hash(hashlib.md5((key+str(j)).encode()).hexdigest())
           if ddddd.search(gen2) and  gen2.find(m.group(1)*5)>-1:
               has_bad=False
               break
       if not has_bad:
           k+=1
           if k==65:
               break
           print(k,j,i,gen,gen2)
"""

for i in range(1_000_000):
    print(i, streched_hash(hashlib.md5((key+str(i)).encode()).hexdigest() ) )

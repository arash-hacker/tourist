from itertools import permutations
f=open('9.txt','r')
f=f.read()
nodes=set()
edges=[]
for st in f.splitlines():
    x,_,y,_,dist=st.split(' ')
    dist=int(dist)
    nodes.add(x)
    nodes.add(y)
    edges.append((x,y,dist))
nodes = sorted(list(nodes))

g = dict([(node, {}) for node in nodes])
for edge in edges:
    loc1, loc2, dist = edge
    g[loc1][loc2] = dist
    g[loc2][loc1] = dist

paths = []
print(g)
raise Exception()
for i, path in enumerate(permutations(nodes)):
    distance = 0
    for loc1, loc2 in zip(path[:-1], path[1:]):
        distance += g[loc1][loc2]

    paths.append((distance, path))
paths.sort()
print(paths[0],paths[-1])


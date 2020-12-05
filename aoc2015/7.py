import re
is_number=re.compile(r"[0-9]+$")
f=open("./7.txt","r")
ff=open("./7.txt","r")
l={}
operations=["RSHIFT","LSHIFT","AND","OR","SET","NOT"]

def number_or_node(x):
    if x.isnumeric():
        return int(x)
    if x in l.keys():
        return l[x]
    l[x]=Node(x)
    return l[x]

class Gate:
    def __init__(self,op,operands):
        self.op=op
        self.operands=operands
    def __repr__(self):
        return self.op+"__"+str(self.operands)

class Node:
    def __init__(self,name):
        self.name=name
        self.gate=[]

    def __repr__(self):
        return self.name#+",".join(map(lambda x:str(x),self.gate))

def op_1(command,output):#replacement
    number_or_node(output).gate=Gate("SET",[number_or_node(command[0])])
    

def op_2(command,output):#not
    number_or_node(output).gate=Gate(
        command[0],
        [number_or_node(command[1])]  )

def op_3(command,output):#rs ls and or
    number_or_node(output).gate=Gate(
        command[1],
        [
            number_or_node(command[0]),
            number_or_node(command[2])
        ])

    
op_func={
    1:op_1,
    2:op_2,
    3:op_3,
}
while st:=f.readline():
    st=st.replace('\n','')
    command=st.split(' ')
    op_func[len(command[0:-2])](command[0:-2],command[-1])
i=0
g=[l["a"]]
stack=[]
nodes_stack=[]


############################
for kk in [1,2]:
  if kk == 2:
    l={}
    while st:=ff.readline():
        st=st.replace('\n','')
        command=st.split(' ')
        op_func[len(command[0:-2])](command[0:-2],command[-1])
    l["b"].gate=46065
    g=[l["a"]]
    stack=[]
    nodes_stack=[]
    i=0

    
  while len(g)!=0:
    i=i+1
    # if kk==2:
    #     print("--"+str(i)+"->",g,"\n")
    #     print("++"+str(i)+"->",stack,"\n")
    #     print("^^"+str(i)+"->",nodes_stack,"\n")
    #     print("____________________________")
    n=g[0]
    g=g[1:]
    if type(n) is Node:#node
            nodes_stack.append(n)
            if is_number.match(str(n.gate)) is not None:#is number
                g=["SET"]+g#this impose recalced value doesnt overwrite next gate
            g=[n.gate]+g
    elif type(n) is Gate:#gate
            g=n.operands+[n.op]+g
    else:#number or op ; here we can perform truely number with operations
            stack.append(n)
            if stack[-1] in operations and nodes_stack.__len__()>0:
                last_node=nodes_stack.pop()
                if stack[-1]=="NOT":
                    last_node.gate=~stack[-2]
                elif stack[-1]=="SET":
                    last_node.gate=stack[-2]
                elif stack[-1]=="RSHIFT":
                    if is_number.match(str(last_node.gate)) is None:#is number; overwrite for first time
                        last_node.gate=(stack[-3]>>stack[-2]) & 65535 
                    stack.pop()#value
                elif stack[-1]=="LSHIFT":
                    if is_number.match(str(last_node.gate)) is None:#is number; overwrite for first time
                        last_node.gate=(stack[-3]<< stack[-2]) & 65535
                    stack.pop()#value
                elif stack[-1]=="AND":
                    if is_number.match(str(last_node.gate)) is None:#is number; overwrite for first time
                        last_node.gate=(stack[-3] & stack[-2]  ) & 65535
                    stack.pop()#value
                elif stack[-1]=="OR":
                    if is_number.match(str(last_node.gate)) is None:#is number; overwrite for first time
                        last_node.gate=(stack[-3] | stack[-2]  ) & 65535
                    stack.pop()#value
                g=[last_node.gate]+g
                stack.pop()#command
                stack.pop()#value
    #46065
    #14134
    # for ll,lv in sorted(l.items()) :
    # print(ll,lv.gate)
  print(l["a"].gate)

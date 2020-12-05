f=open("2.txt","r")
sum=0
sum2=0
while st:=f.readline():
    l,w,h=map(lambda x:int(x),st.split('x'))
    #sum+=(2*l*w + 2*w*h + 2*h*l+min(l*w,w*h,h*l))
    sum2+=(w*h*l+2*min(w+l,l+h,h+w))
print(sum2,sum)
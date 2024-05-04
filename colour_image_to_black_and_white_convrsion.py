a=input()
b=input()
l1=[]
for i in a:
    if i not in b:
        l1.append(i)
for j in b:
    if j not in a:
        l1.append(j)
x=len(l1)
print(x)
m="FLAMES"
l2=list(m)
print(l2)
for i in range(1,x):
    for j in range(len(m)):
        c=c+1
        if c==len(l2):
            j=0
            c=c+1
            if c==x:
                l2.pop(l2[c])
print(l2)


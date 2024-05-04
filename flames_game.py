a=input()
b=input()
l1=[]
c=0
for i in a:
    if i not in b:
        l1.append(i)
for j in b:
    if j not in a:
        l1.append(j)
x=len(l1)
#print(x)
s="FLAMES"
while len(s)!=1:
    i=(x%len(s))-1
    if i>=0:
        s=s[i+1:]+s[:i]
    else:
        i=len(s)+i
        s=s[:i]
print(s)
    

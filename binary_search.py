l=[1,3,5,7,9]
si=0
li=len(l)-1
se=9
while si<=li:
    mid=(si+li)//2
    if l[mid]==se:
        print("ele found")
        break
    elif se>l[mid]:
        si=mid+1
    else:
        li=mid-1
else:
    print("ele not found")

    

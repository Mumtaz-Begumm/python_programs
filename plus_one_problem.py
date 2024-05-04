digits=[9,9]
l=[]
s = [str(i) for i in digits]
print(s)
res = int("".join(s))
res=res+1
#digits.clear()
print(digits)
digits.append(res)
#print(digits)
for i in range(len(digits)):
    l=list(map(int,str(digits[i])))
print(l)

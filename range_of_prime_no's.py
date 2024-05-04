def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
print("enter the starting number:")
a=int(input())
print("enter the last number:")
b=int(input())
for i in range(a,b+1):
    if isprime(i):
        print(i)
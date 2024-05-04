print("enter a number:")
n=int(input())
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum=sum*10+rem
print(sum)
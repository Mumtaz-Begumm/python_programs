print("enter a number:")
n=int(input())
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
if(temp==sum):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
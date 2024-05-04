'''print("enter a year")
y=int(input())
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print("it is a leap year")  
        else:
            print("it is not a leap year")  
    else:
         print("it is a leap year")   
else:
    print( y,"is not a leap year") '''




#another method
'''print("enter a year")
year=int(input())
if(year %100==0 and year%400==0):
    print("leap year")
elif(year%100!=0 and year%4==0):
    print("leap year")
else:
    print("not a leap year")'''


#another method
print("enter a year")
year=int(input())
if(year%400==0 or year%100!=0 and year%4==0):
    print("it is a leap year")
else:
    print("not a leap year")




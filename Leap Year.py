#verify leap year
print("\nChoose the Following option givdn below")
print("\n1 Month\n2 Day \n3 Year")
number=int(input("enter the number"))
if number==1:
    month = int(input("enter the no of days in february"))
    if month==29:
     print("the year is leap")
    else:
        print("Not Leap year")
elif number==2:
   day = int(input("enter the total days in year"))
   if day==366:
    print("year is leap")
   else:
       print("Not Leap year")
elif number==3:
    year = int(input("enter the year"))
    if year%4==0:
     print("leap year")
    else:
        print("Not Leap year")
else:
    print("not leap year")

#square or rectangle
a=float(input("insert a"))
print(a)
b=float(input("insert b"))
print(b)
if a==b:
    print("it is a square")
else:
    print("it is rectangle")

#who is eldest
age1=int(input("enter age1"))
age2=int(input("insert age2"))
age3=int(input("insert age3"))

if (age1>age2) and (age1>age3):
    largest=age1
elif (age2>age1) and (age2>age3):
    largest=age2
else:
    largest=age3
    print("largest number is",largest)
#insertng age,sex and condition
a=int(input("enter the age"))
b=input("enter the sex is male or female")
c=input("enter your marital status")
print(c)
if b=='f':
    print("work only in urban area")
elif b=='m':
    if 20 < a <= 40:
        print("he may work in anywhere")
    elif 40<a<60:
        print("work only in urban areas")
    else:
        print("eror ocured")






#loops
c=[]
for i in range(0,10):
    b=int(input("enter the number"))


    c.append(b)

print("you enterd folowing numbers")
print(b)

#make a list by user and orint its square
z=[]
d=[]
for i in range(0,4):
    b=int(input("enter the number"))
    z.append(b)
print("you enterd the following number")
print(z)
for i in z:
    x=pow(i,2)
    d.append(x)
print(d)













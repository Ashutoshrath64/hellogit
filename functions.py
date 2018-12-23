#question 1
#area of sphear is
pi=3.14
def area_sphere(r):
    area=4*pi*r*r
    return area
ans=area_sphere(5)
print("area is equal to",ans)
#question 2
n=int(input("enter the number"))
for i in range(0,11):
    print(n*i)
#quiestion 3
def power(x,y):
    if y==1:
        return x
    else:
        return x*power(x,y-1)
x=3
y=4
print("result",power(x,y))
#perfect number
list=[]
n=6
for i in range(1,10):
     x=n%i

     if x==0:

       print(i,end="")
       list.append(i)

print(list)
b=len(list)
c=0
for i in list[0:b-1]:
    j=c
    c=i+j

print(c)
d=1
for i in list[0:b-1]:
    j=d
    d=i*j

print(d)
if c==d:
    print("numer is perfect")
else:
    print("number is not perfect")



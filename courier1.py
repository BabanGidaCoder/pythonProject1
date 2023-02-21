pkg_price=int(input("Enter the value of package: "))

dist=int(input("Enter the distance for the package delivery(Km.)): "))

print("Select a shipping method:\n1. Air shipping \n2. Freight shipping")

c=int(input())

cost = 0

if (c==1):

cost = 0.36

elif (c==2):

cost = 0.25

print("Select insurance type:\n1. Full type insurance \n2. limited type insurance")

c1=int(input())

ins_cost = 0

if(c1==1):

ins_cost = 50

elif(c1==2):

ins_cost = 25

print("Select if you want to add a gift:\n1. Yes \n2. No")

c2=int(input())

g_cost = 0

if(c2==1):

g_cost = 15

elif(c2==2):

g_cost = 0

print("Select a type of delivery:\n1. Priority delivery \n2. Standard delivery")

c3=int(input())

deli_cost=0

if(c3==1):

deli_cost = 100

elif(c3==2):

deli_cost = 20

total = pkg_price + dist*cost + ins_cost + g_cost + deli_cost

print("Total cost for the package is: ",total)

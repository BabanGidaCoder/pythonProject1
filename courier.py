price = int(input(" Enter the price of the package you would like:"))
total_dist = int(input("Enter the total distance of the delivery in Kms:"))

#air = 0.36
#freight = 0.25
#full_insurance = 50.00
#lim_insurance = 25.00
#gift = 15.00
#no_gift = 0.00
#priority = 100.00
#standard_del = 20.00

print("select a shipping method:\n1. Air \n2. Freight")

delivery_cost = int(input())    #prompt from choice of shipping
cost = 0
if delivery_cost == 1:
    cost = 0.36
elif delivery_cost == 2:
    cost = 0.25


print("Select insurance type:\n1. Full type insurance \n2. limited type insurance")

delivery_cost1 = int(input())

ins_cost = 0

if delivery_cost1 == 1:

    ins_cost = 50

elif delivery_cost1 == 2:

    ins_cost = 25
print("Select if you want to add a gift:\n1. Yes \n2. No")

delivery_cost2 = int(input())

g_cost = 0

if delivery_cost2 == 1:

    g_cost = 15

elif delivery_cost2 == 2:

    g_cost = 0
print("Select a type of delivery:\n1. Priority delivery \n2. Standard delivery")

delivery_cost3 = int(input())

deli_cost = 0

if delivery_cost3 == 1:

    deli_cost = 100

elif delivery_cost3 == 2:

    deli_cost = 20
total = price + total_dist * cost + ins_cost + g_cost + deli_cost

print("Total cost for the package is: ", total)

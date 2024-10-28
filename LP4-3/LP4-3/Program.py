eggs = int(input("Enter # of eggs: "))
price = 0.0
cost = 0.0

if eggs < 4:
    price = 0.50
elif eggs < 6:
    price = 0.45
elif eggs < 11:
    price = 0.40
elif eggs >= 11:
    price = 0.35
else:
    print("invalid # of eggs")


cost = eggs * price
print("Cost is $" + str(round(cost,2)))

input()
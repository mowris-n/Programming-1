eggs = int(input("Enter amount of eggs: "))
price = 0.0
cost = 0.0

if eggs < 48:
    price = 0.50
elif eggs < 72:
    price = 0.45
elif eggs < 132:
    price = 0.40
elif eggs >= 132:
    price = 0.35
else:
    print("invalid amount of eggs")


cost = (eggs * price) / 12
print("Cost is $" + str(round(cost,2)))

input()
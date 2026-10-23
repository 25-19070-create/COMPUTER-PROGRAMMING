total = 0
items = 0
price = float(input("Price (0 to stop): "))
while price != 0:
    total += price
    items += 1
    price = float(input("Price (0 to stop): "))
if items > 0:
    average = total / items
else:
    average = 0
print("Items:", items)
print("Total: {:.2f}".format(total))
print("Average: {:.2f}".format(average))25
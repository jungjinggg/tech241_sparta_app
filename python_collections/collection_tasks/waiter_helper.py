starters = ["crab cakes", "prawn cocktail", "nachos"]
mains = ["pizza", "spaghetti", "steak"]
desserts = ["ice cream", "apple pie", "chocolate cake"]

# Menu
print(f'the starter menu: {starters}')
print(f'the main course menu: {mains}')
print(f'the dessert menu: {desserts}')

starter_order = input("What would you like for your starter?: ")
main_order = input("What would you like for your main course? ")
dessert_order = input("What would you like for your dessert?: ")

order = []
for i in starters:
    if i == starter_order:
        order.append(i)

for i in mains:
    if i == main_order:
        order.append(i)

for i in desserts:
    if i == dessert_order:
        order.append(i)


print(f'your starter: {order[0]}')
print(f'your main course: {order[1]}')
print(f'your dessert: {order[-1]}')




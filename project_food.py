menu = {
    'Tea': 15,
    'Coffee': 30,
    'Burger': 80,
    'Pucka': 40,
    'Coke': 25,
    'Banana':10,
    'Pasta':50,
}

print("Welcome to Sajid Restaurant.")
print("Here is our menu!")
for item, price in menu.items():
    print(f"{item} : {price} Tk")

total_tk = 0
orders = []

while True:
    item = input("\nWhat would you like to order, Sir? ").strip().title()
    
    if item in menu:
        print(f"Your {item} has been ordered.")
        total_tk += menu[item]
        orders.append(item)
    else:
        print("Sorry, this item is not available in our restaurant.")
    
    another = input("Would you like to order anything else? (YES/NO): ").strip().lower()
    if another == "no":
        break

print("\n----- Order Summary -----")
for i, food in enumerate(orders, start=1):
    print(f"{i}. {food} - {menu[food]} Tk")
print(f"Total Bill = {total_tk} Tk")
print("Thank you for visiting Sajid Restaurant!")

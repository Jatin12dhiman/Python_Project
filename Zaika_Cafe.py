print("Welcome in Laxmi Sweets")
menu={
    "rosgulla": 25,
    "gulabjamun": 20,
    "rajbhog":30,
    "kajukatli":25,
    "samosa":10,
    "chowmein":50,
    "samosachaat":40,
    "colddrink":50,
    "tikkichaat":50
}

print("Our Menu: ")
print("-----------")
total_order = 0
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

next_order = True

while next_order:
    order = input("Enter the name of item you want to add in your order: ").lower()
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
        another_order = input("Do you want to add another item? press (yes/no): ").lower()
        if another_order == "yes":
            next_order = True
        else:
            next_order = False
    else:
        print(f"{order} is not available")
        another_order = input("Do you want to add another item? press (yes/no): ").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total bill is: Rs.{total_order}")